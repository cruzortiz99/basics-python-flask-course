function listenAll(querySelector) {
  return eventName =>
   eventListener => {
    return document.querySelectorAll(querySelector).forEach((htmlElement, index)=> htmlElement.addEventListener(eventName, (event) => eventListener(event, index)))
  }
}
function getUserName(route) {
  return (position) => route.split('/').slice(position)[0]
}
function taskRemoveButtonEventListener(event, index ) {
  console.log(event,index)
}
function taskCheckboxEventListener(event, index) {
  console.log(event, index)
}

listenAll('.button.remove.task')('click')(taskRemoveButtonEventListener)
listenAll('.checkbox.task')('change')(taskCheckboxEventListener)
console.log(getUserName(window.location.toString())(-1))