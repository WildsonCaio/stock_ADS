let picture = document.querySelector('.picture')
let loadPicture = document.querySelector('.load-picture')

loadPicture.addEventListener('change', (e)=>{
    picture.src = URL.createObjectURL(e.target.files[0])
})