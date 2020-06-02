function compose( ...functions ) {
  return functions.reduceRight((prev,current) => current(prev))
}

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
      xhttp.open( 'POST', url, true )
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

function redirectTo( url ) {
  return ( pathParameters ) => window.location.replace( `${url}/${pathParameters.join( '/' )}` )
}