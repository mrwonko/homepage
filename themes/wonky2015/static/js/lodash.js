angular.module( 'lodash', [] )
.factory( '_', function( $window ) {
    var _ = $window._;
    delete( $window._ );
    return _;
} )
.run( function( _ ) {
    // force factory to be run at bootstrap, removing global _ variable
} )
;
