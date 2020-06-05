const buttons = document.querySelectorAll('.button.remove.task').forEach((button, key) => {
  button.addEventListener('click', event => {
    console.log(event.target, key)
  })
})