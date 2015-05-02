// second parameter is list of required modules, omitting it turns this into a module lookup instead of a definition.
angular.module( 'commentsApp', [ 'lodash', 'ngSanitize', 'backend' ] )
.controller( 'CommentListCtrl', function( $scope, _, backend, post ) {
    $scope.comments = []
    $scope.loading = true
    $scope.error = null
    backend.getComments( post )
    .success( function( data, status, headers, config ) {
            $scope.loading = false
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
            $scope.error = data;
    } )
} )
;
