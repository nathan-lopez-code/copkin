class Card{
    constructor() {
        this.card = localStorage.getItem("card");
        if (this.card == null){
            this.card =  [];
        }else{
            this.card = JSON.parse(this.card)
        }
    }

    save(){
        localStorage.setItem("card", JSON.stringify(this.card));
    }

    addToCard(article){
        let foundArticle = this.card.find(a => a.id === article.id);
        if (foundArticle !== undefined){
            foundArticle.quantity++;
        }else{
            article.quatity = 1;
            this.card.push(article)
        }
        this.save();
    }
    removeProduit(produit) {
        this.card = this.card.filter(a => a.id !== produit.id);
        this.save()
    }

    changeQuatity(article, setQuatity) {
        let foundArticle = this.card.find(a => a.id === article.id);
        if (foundArticle !== undefined) {
            foundArticle.quatity += setQuatity;
            if (foundArticle.quatity <= 0) {
                this.removeProduit(foundArticle);
            } else {
                this.save()
            }
        }
    }
    checkArticle(article){
        return this.card.find(a => a.id === article.id);
    }

    getNumberAricle(){
        let number = 0;
        for (let article of this.card){
            number += article.quatity;
        }
        return number;
    }
    getTotalPrice(){
        let total = 0;
        for (let article of this.card) {
            total += article.quatity * article.price;
        }
        return total
    }

}

function initState(card, cartContainer){
    let article = [];

    if (card.getNumberAricle() !== 0){
        for (let i = 0; i < card.getNumberAricle(); i++){
            article = card.card[i];
              cardItem_ =  '<div class="card mb-3">'+
'                 <div class="card-body">'+
'                   <div class="d-flex justify-content-between">'+
'                     <div class="d-flex flex-row align-items-center">'+
'                       <div>'+
'                         <img'+
'                           src="'+ article['image'] +'"'+
'                           class="img-fluid rounded-3" alt="Shopping item" style="width: 90px;">'+
'                       </div>'+
'                       <div class="ms-3" >'+
'                         <h6 class="ml-1"> <a href="'+ article['url'] +'">'+ article['name'] +'</a> </h6>'+
'                       </div>'+
'                     </div>'+
'                     <div class="d-flex flex-row align-items-center">'+
'                       <div style="width: 50px;">'+
'                         <p class="fw-normal mb-0">'+ article['quatity']+'</p>'+
'                       </div>'+
'                       <div style="width: 80px;">'+
'                         <p class="mb-0">'+ article['price'] +'$ </p>'+
'                       </div>'+
'                       <button type="submit" data-id="'+ article['id'] +'" id="removebtn" style="color: #f60e0e;border: none"><i class="fas fa-trash-alt"></i></button>'+
'                     </div>'+
'                   </div>'+
'                 </div>'+
'               </div>';
                try{
                    cartContainer.innerHTML += cardItem_;
                } catch (e) {

                }


        }
        let removebtn = document.querySelectorAll("#removebtn")
        let numberArticle = document.querySelector("#numberProduct");
        let navPanier = document.querySelector("#nav-panier");

        removebtn.forEach((btn)=>{
            btn.addEventListener('click', () => {
                let art = {
                    "id": btn.getAttribute('data-id'),
                }
                card.removeProduit(art);
                numberArticle.innerHTML = card.getNumberAricle().toString();
                navPanier.innerText = card.getNumberAricle();

                cartContainer.innerHTML = " ";
                if (card.getNumberAricle() === 0){
                    initPrice(card);
                }

                initState(card, cartContainer);
            })
        })
        initPrice(card)


    } else {
        let html = document.createElement('div');
        try{
            document.querySelector(".NumberAricle").style.display = "none";
            html.innerHTML = ' <div class="card mb-3"> <p class="text-center"> Aucun article dans le panier, veillez en ajouter</p> </div>';
            cartContainer.appendChild(html)
        } catch (e) {

        }


    }
}

function initPrice(card){
    let total = document.querySelector("#total")
    let numberArticle = document.querySelector("#numberArticle");

    numberArticle.innerText = card.getNumberAricle();
    if(card.getNumberAricle() === 0){
        total.innerText = '0 $';

    } else {
        total.innerText = card.getTotalPrice().toString() + '$';
    }

}

function getCookie(name) {
    var cookieValue = null;
    if (document.cookie && document.cookie !== '') {
        var cookies = document.cookie.split(';');
        for (var i = 0; i < cookies.length; i++) {
            var cookie = jQuery.trim(cookies[i]);
            // Does this cookie string begin with the name we want?
            if (cookie.substring(0, name.length + 1) === (name + '=')) {
                cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                break;
            }
        }
    }
    return cookieValue;
}


async function postCard(cardData){
    let origin = window.location.origin
    let xmlhttp = new XMLHttpRequest()

    try{
      xmlhttp.open("POST", origin + '/sellPanier')
      xmlhttp.setRequestHeader( "X-CSRFToken", getCookie("csrftoken"));

      xmlhttp.send(JSON.stringify(cardData))
        
    } catch (error) {
        console.error("Error;", error);
    }
}


(function (){

    let card = new Card();
    let messageCard = document.querySelector(".pop");
    let numberArticle = document.querySelector("#numberProduct");
    let messagePop = document.querySelector(".messagePop");
    let navPanier = document.querySelector("#nav-panier")
    numberArticle.innerHTML = card.getNumberAricle().toString();


    document.querySelectorAll(".add-to-card").forEach(
        (button)=>{
            button.addEventListener("click", ()=>{
                let article = {
                    "id" : button.getAttribute('data-id'),
                    "name" : button.getAttribute('data-name'),
                    "price" : button.getAttribute('data-price'),
                    "quantity" : 1,
                    "image" : button.getAttribute('data-image'),
                    "url" : button.getAttribute('data-url')
                }
                let articleCard = card.checkArticle(article)
                if (articleCard === undefined){
                    messagePop.innerHTML = "vous avez ajouter <strong>" + article['name'] + "</strong> au pannier"

                } else{
                    messagePop.innerHTML = "quantité pour <strong>" + article['name'] + "</strong> mise à jour"
                }
                card.addToCard(article);
                numberArticle.innerHTML = card.getNumberAricle().toString();
                navPanier.innerText = card.getNumberAricle();
                messageCard.classList.remove("d-none");
                setTimeout(function() {
                    messageCard.classList.add("d-none");
                }, 3000);

            })
        }
    )

})();


(function(){

    let card = new Card();
    try{
        let cartContainer = document.querySelector("#cartContainer");
        initState(card, cartContainer)
    } catch (e) {

    }

})();


(function(){
    let card = new Card();
    let cardData = card.card;
    try {
        let btnCard = document.querySelector("#btn-card");

        btnCard.addEventListener("click", ()=>{
            postCard(cardData);
        })
    } catch (e) {
        
    }

})();


