// definitely typed references
/// <reference path="../../definitelytyped/angularjs/angular.d.ts" />

angular.module( 'backend', [ 'templateGenerated' ] )
.factory( 'backend', function ( backendUrl, $http ) {
    return {
        "getComments": function( post ) {
            /// <summary>Retrieves comments from the backend</summary>
            /// <param name="post" type="string">Post to retrieve comments for</param>
            return $http.get( backendUrl + "/rest/blog/" + post + "/comments" );
        }
    };
} )
;
