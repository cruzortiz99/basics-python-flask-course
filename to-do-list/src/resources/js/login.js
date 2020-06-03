  function connectForm(form, url) {
    return compose( post( url ),formValidator ,extractFormValues)(document.forms[ form ] )
  }

  function register () {
    try {
      return connectForm('loginForm', '/register').then( response => {
        redirectTo( '/to-do' )( [ response[ 'user_name' ] ] )
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
        redirectTo('/to-do')([response['user_name']])
      })
    }catch(error) {
      alert(error)
    }
  }

  function addLoginFormListener(form) {
    return (handler) => {
      return form.addEventListener('submit', handler)
    }
  }
  
  function login() {
    return addLoginFormListener(document.forms['loginForm'])(loginHandler)
  }

  function formValidator(formValues) {
    if (!sizeValidator(8)(formValues['password'])) {
      throw Error('Password must be larger than 8 characters')
    }
    if (!sizeValidator(2)(formValues['user_name'])) {
      throw Error('User must have more than 2 characters')
    }
    return formValues
  }

  login()