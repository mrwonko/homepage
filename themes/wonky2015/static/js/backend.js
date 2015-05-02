angular.module( 'backend', [ 'templateGenerated' ] )
.factory( 'backend', function( backendUrl, $http ) {
    var backend = {
        "getComments": function( post ) {
            return $http.get( backendUrl + "/rest/blog/" + post + "/comments" )
        }
    };
    return backend;
} )
;