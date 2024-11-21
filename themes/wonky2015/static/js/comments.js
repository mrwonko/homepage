// definitely typed references
/// <reference path="../../definitelytyped/angularjs/angular.d.ts" />
/// <reference path="../../definitelytyped/lodash/lodash.d.ts" />

// second parameter is list of required modules, omitting it turns this into a module lookup instead of a definition.
angular.module( 'commentsApp', [ 'lodash', 'ngSanitize', 'templateGenerated' ] )
.controller( 'CommentListCtrl', function( $scope, _, backendUrl, $http, post ) {
    ///<summary>Controller for list of comments</summary>
    ///<param name="backend" type="string"></param>
    $scope.comments = [];
    $scope.loading = true;
    $scope.error = null;
    $http.get( backendUrl + "/rest/blog/" + post + "/comments" )
    .success( function( data, status, headers, config ) {
            $scope.loading = false;
            if( headers( "Content-Type" ) != "application/json" ) {
                $scope.error = "Server did not send json!";
                return;
            }
            _.each( data.comments, function( comment ) {
                comment[ "time" ] = new Date( comment[ "time" ] )
            } );
            $scope.comments = _.sortBy( data.comments, 'time' );
    } )
    .error( function( data, status, headers, config ) {
            $scope.loading = false;
            $scope.error = status == 0 ? 'Connection refused.' : 'Error ' + status + '.';
    } );
} )
.controller( 'newCommentCtrl', function( $scope, backendUrl, $http, post ) {
    $scope.comment = {
        "author": "",
        "content": "",
        "email": "",
        "url": ""
    };
    $scope.loading = false;
    $scope.error = null;
    $scope.submitted = false;
    $scope.submit = function() {
        $scope.loading = true;
        $http.post( backendUrl + "/rest/blog/" + post + "/comments", $scope.comment )
        .success( function( data, status, headers, config ) {
            $scope.loading = false;
            if( data.spam ) {
                $scope.error = "You appear to be a spammer. Boo! Boo!";
            } else {
                $scope.error = null; // dismiss potential previous errors
                $scope.submitted = true;
            }
        })
        .error( function( data, status, headers, config ) {
            $scope.loading = false;
            $scope.error = status == 0 ? 'Connection refused.' : 'Error ' + status + ': ' + data;
        } );
    };
    $scope.dismissError = function() {
        $scope.error = null;
    };
} );
;
