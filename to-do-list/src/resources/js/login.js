function extractFormValues( form ) {
    const formValues = {
      user_name: form[ 'user_name' ].value,
      password: form[ 'password' ].value
    }
    return formValues
  }

  function post( url ) {
    return function ( values ) {
      return new Promise( ( resolve, reject ) => {
        const xhttp = new XMLHttpRequest()
        xhttp.open( 'POST', '/register', true )
        xhttp.setRequestHeader( 'Content-type', 'application/json' )
        xhttp.send( JSON.stringify( values ) )
        xhttp.onreadystatechange = function () {
          if ( this.status >= 300 ) {
            reject( 'Error' )
          }
          if ( this.readyState === 4 && this.status === 200 ) {
            resolve( JSON.parse( this.response ) )
          }
        }
      } )
    }
  }

  function compose( f, g, x ) {
    return f( g( x ) )
  }

  function redirectTo( url ) {
    return ( pathParameters ) => window.location.replace( `${url}/${pathParameters.join( '/' )}` )
  }

  function register() {
    const response = compose( post( '/register' ), extractFormValues, document.forms[ 'loginForm' ] ).then( response => {
      redirectTo( '/to-do' )( [ response[ 'user_name' ] ] )
    } ).catch( error => {
      console.error( error )
    } )
  }