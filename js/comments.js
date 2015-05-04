/// <reference path="../definitelytyped/angularjs/angular.d.ts" />
/// <reference path="../definitelytyped/angularjs/angular-sanitize.d.ts" />

angular.module( "commentsAdminApp", [ "ngSanitize" ] )
.controller( "commentsCtrl", function( $scope, $http ) {
	$scope.comments = [];
	$scope.error = null;
	$scope.success = null;
	$scope.dismissError = function() {
		$scope.error = null;
	}
	$scope.dismissSuccess = function() {
		$scope.success = null;
	}
	$scope.moderate = function( comment, action ) {
		comment.loading = true;
		$http.post( "rest/blog/comments/" + comment.id, { action: action } )
		.success( function( data, status, headers, config ) {
			comment.loading = false;
			if( !data.success ) {
				$scope.error = "Server reported failure.";
			} else {
				$scope.comments.splice( $scope.comments.indexOf( comment ), 1 );
				$scope.success = "Comment is " + action
			}
		} )
		.error( function( data, status, headers, config ) {
			comment.loading = false;
			$scope.error = "Error " + status;
		} );
	};
	$scope.date = function( date ) {
		return new Date( date ).toLocaleString();
	}
	$scope.loading = true;
	$http.get( "rest/blog/comments/unapproved" )
	.success( function( data, status, headers, config ) {
		$scope.comments = data.comments;
		$scope.loading = false;
	} )
	.error( function( data, status, headers, config ) {
		$scope.error = "Error " + status + " loading comments!";
		$scope.loading = false;
	} );
} )
;