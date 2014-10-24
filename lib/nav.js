/*
	Navigation module; active page, title etc.
*/

angular.module( "nav", [ "ngRoute" ] )
.constant( "pages",
	[ { name : "Home",      url : "/home",      title : "Mr. Wonko's Website",   template: "partials/home.html" }
	, { name : "Blog",      url : "/blog",      title : "Mr. Wonko's Blog",      template: "partials/blog.html" }
	, { name : "Downloads", url : "/downloads", title : "Mr. Wonko's Downloads", template: "partials/downloads.html" }
	, { name : "Games",     url : "/games",     title : "Mr. Wonko's Games",     template: "partials/games.html" }
	, { name : "Portfolio", url : "/portfolio", title : "Mr. Wonko's Portfolio", template: "partials/portfolio.html" }
	//, { name : "Forum",     url : "forum" }
	, { name : "About Me",  url : "/about",     title : "About Mr. Wonko",       template: "partials/about.html" }
	] )
.controller( "navCtrl", [ "$scope", "$route", "pages", function( $scope, $route, pages ) {
	var now = new Date();
	$scope.date =
		{ year : now.getFullYear()
		, month : now.getMonth()
		, day : now.getDate()
		};
	$scope.pages = pages;
	$scope.on
	$scope.$on( "$routeChangeSuccess", function(  ) {
		console.log( $route.current );
		$scope.currentPage = _.find( pages, { url: $route.current.$$route.originalPath } ) || pages[ 0 ];
		} )
	$scope.showImprint = function() {
		// TODO
	};
} ] )
.config( [ "$routeProvider", "pages", function( $routeProvider, pages ) {
	_.forEach( pages, function( page ) {
		$routeProvider.when( page.url,
			{ templateUrl: page.template
			});
	});
	$routeProvider.otherwise(
		{ redirectTo: "/home"
		} );
} ] )
;
