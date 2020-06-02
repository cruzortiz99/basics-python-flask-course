  function connectForm(form, url) {
    return compose( post( url ), extractFormValues)(document.forms[ form ] )
  }

  function register () {
    return connectForm('loginForm', '/register').then( response => {
      redirectTo( '/to-do' )( [ response[ 'user_name' ] ] )
    } ).catch( error => {
      console.error( error )
    } )
  }

  function login() {
    return connectForm('loginForm', '/login').then(response => {
      redirectTo('/to-do')(response['user_name'])
    }).catch(error => {
      console.error(error)
    })
  }