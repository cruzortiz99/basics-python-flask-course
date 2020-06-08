function getUserName(route) {
  return (position) => route.split('/').slice(position)[0]
}

function getUserNameInToDoURL(position) {
  return getUserName(window.location.toString())(position)
}

function taskRemoveButtonEventListener(event) {
  const taskId = event.target.getAttribute('id').split('-')[0]
  const userName = getUserNameInToDoURL( -1 )
  deleteRaw(`/to-do/${userName}/${taskId}`)().then((response) => {
    window.location.reload()
  }).catch(error => console.error(error))
}

function taskCheckboxEventListener(event) {
  const taskId = event.target.getAttribute('id').split('-')[0]
  const userName = getUserNameInToDoURL( -1 )
  updateRaw(`/to-do/${userName}/${taskId}`)().then((response) => {
    window.location.reload()
  }).catch(error => console.error(error))
}

function newTodoEventListener(event) {
  event.preventDefault()
  const task = {name: event.target['name'].value}
  const userName = getUserNameInToDoURL(-1)
  post(`/to-do/${userName}`)(task).then(()=> {
    window.location.reload()
  }).catch(error => console.error(error))
}

function refresh(event) {
  window.location.reload()
}

function logoutListener (event) {
  event.preventDefault()
  redirectTo('/login')([])
}

listenAll('.button.danger')('click')(taskRemoveButtonEventListener)
listenAll('.checkbox')('change')(taskCheckboxEventListener)
listenAll('#refresh')('click')(refresh)
listenAll('#new_todo')('submit')(newTodoEventListener)
listenAll('#logout')('click')(logoutListener)