// ==============================
// Scroll To Top Button
// ==============================

const topBtn = document.getElementById("topBtn");

window.addEventListener("scroll", () => {

    if (window.scrollY > 300) {
        topBtn.style.display = "block";
    } else {
        topBtn.style.display = "none";
    }

});

topBtn.onclick = () => {

    window.scrollTo({
        top: 0,
        behavior: "smooth"
    });

};


// ==============================
// Navbar Shadow
// ==============================

const navbar = document.querySelector(".navbar");

window.addEventListener("scroll", () => {

    if (window.scrollY > 50) {

        navbar.style.boxShadow = "0 5px 25px rgba(0,0,0,.4)";

    } else {

        navbar.style.boxShadow = "none";

    }

});


// ==============================
// Fade Animation
// ==============================

const sections = document.querySelectorAll("section");

const observer = new IntersectionObserver((entries)=>{

    entries.forEach(entry=>{

        if(entry.isIntersecting){

            entry.target.style.opacity="1";
            entry.target.style.transform="translateY(0)";

        }

    });

},{
    threshold:0.2
});

sections.forEach(section=>{

    section.style.opacity="0";
    section.style.transform="translateY(80px)";
    section.style.transition="1s";

    observer.observe(section);

});


// ==============================
// Typing Effect
// ==============================

const text = [
    "Graphic Designer",
    "Logo Designer",
    "Poster Designer",
    "Photo Editor"
];

let i = 0;
let j = 0;
let current = "";
let isDeleting = false;

const typing = document.querySelector(".hero-content h2");

function type(){

    if(!typing) return;

    current = text[i];

    if(!isDeleting){

        typing.textContent = current.substring(0,j++);
    }else{

        typing.textContent = current.substring(0,j--);

    }

    if(!isDeleting && j === current.length+1){

        isDeleting=true;

        setTimeout(type,1200);

        return;

    }

    if(isDeleting && j===0){

        isDeleting=false;

        i++;

        if(i===text.length){

            i=0;

        }

    }

    setTimeout(type,isDeleting?50:100);

}

type();