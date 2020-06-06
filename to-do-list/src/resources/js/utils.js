function compose( ...functions ) {
  return (value) => functions.reduceRight((prev,current) => current(prev),value)
}

function request (method) {
  return function (url) {
    return function ( values ) {
      return new Promise( ( resolve, reject ) => {
        const xhttp = new XMLHttpRequest()
        xhttp.open( method, url, true )
        xhttp.setRequestHeader( 'Content-type', 'application/json' )
        xhttp.send( JSON.stringify( values ) )
        xhttp.onreadystatechange = function () {
          if ( this.status >= 300 ) {
            reject( `Error: ${status}` )
          }
          if ( this.readyState === 4 && this.status === 200 ) {
            resolve( JSON.parse( this.response ) )
          }
        }
      } )
    }
  }
}

function post( url ) {
  return request('POST')(url)
}

function deleteRaw (url) {
  return request('DELETE')(url)
}

function updateRaw (url) {
  return request('PATCH')(url)
}

function redirectTo( url ) {
  return ( pathParameters ) => 
    window.location.assign(
      `${url}${pathParameters && pathParameters.length > 0 ? `/${pathParameters.join('/')}`: ''}`
    )
}

function sizeValidator (maxSize) {
  return (value) => {
    return !!value.trim() && value.length > maxSize
  }
}

function listenAll(querySelector) {
  return eventName =>
   eventListener => 
    document.querySelectorAll(querySelector).forEach((htmlElement, index)=> htmlElement.addEventListener(eventName, (event) => eventListener(event, index)))
}