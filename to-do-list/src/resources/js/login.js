function extractFormValues( form ) {
  const formValues = {
    name: form[ 'name' ].value,
    password: form[ 'password' ].value
  }
  return formValues
}

function connectForm(form, url) {
  return compose( post( url ),formValidator ,extractFormValues)(document.forms[ form ] )
}

function register () {
  try {
    return connectForm('loginForm', '/register').then( response => {
      redirectTo( '/to-do' )( [ response[ 'name' ] ] )
    } ).catch( error => {
      console.error( error )
    } )
  } catch(error) {
    alert(error)
  }
}

function loginHandler(event) {
  event.preventDefault()
  try {
    return connectForm('loginForm', '/login').then(response => {
      redirectTo('/to-do')([response['name']])
    }).catch(()=> alert('User not found')) 
  }catch(error) {
    alert(error)
  }
}

function formValidator(formValues) {
  if (!sizeValidator(8)(formValues['password'])) {
    throw Error('Password must be larger than 8 characters')
  }
  if (!sizeValidator(2)(formValues['name'])) {
    throw Error('User must have more than 2 characters')
  }
  return formValues
}

listenAll('#loginForm')('submit')(loginHandler)
listenAll('#register-button')('click')(register)