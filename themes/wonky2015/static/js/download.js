// definitely typed references
/// <reference path="../../definitelytyped/angularjs/angular.d.ts" />
/// <reference path="../../definitelytyped/lodash/lodash.d.ts" />

// second parameter is list of required modules, omitting it turns this into a module lookup instead of a definition.
angular.module( 'downloadApp', [ 'templateGenerated' ] )
.controller( 'DownloadCtrl', function( $scope, backendUrl, $http, filename, $log ) {
    $scope.downloadCount = "[retrieving]";
    $http.get( backendUrl + "/rest/downloads/" + filename )
    .success( function( data, status, headers, config ) {
            if( headers( "Content-Type" ) != "application/json" ) {
                $scope.downloadCount = "[Error]";
                $log.warn("Server did not send json!");
                return;
            }
            $scope.downloadCount = data.downloads;
    } )
    .error( function( data, status, headers, config ) {
            $scope.downloadCount = "[Error]";
            $log.warn( status == 0 ? 'Connection refused.' : 'Error ' + status + '.' );
    } );
} )
;
