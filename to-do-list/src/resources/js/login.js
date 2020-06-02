  function register() {
    return compose( post( '/register' ), extractFormValues, document.forms[ 'loginForm' ] ).then( response => {
      redirectTo( '/to-do' )( [ response[ 'user_name' ] ] )
    } ).catch( error => {
      console.error( error )
    } )
  }