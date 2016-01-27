(function() {
  "use strict";

  var meubisApp = angular.module('meubisApp', ['ui.router', 
                                       'ngResource', 
                                       'ngAnimate', 
                                       'angularFileUpload',
                                       'relativeDate',
                                       'infinite-scroll',
                                       'mm.foundation',
                                       'angular-capitalize-filter',
                                       ]);

  // Initialize Foundation
  meubisApp.run(function($rootScope, djangoConstants){
    $rootScope.$apply($(document).foundation());

    // Add the current user to the rootScope
    $rootScope.user = djangoConstants.user;

    /** Alerts ************************************************************************/
    $rootScope.alerts = [
    ];

    $rootScope.addAlert = function() {
      
    };

    $rootScope.closeAlert = function(index) {
      $rootScope.alerts.splice(index, 1);
    };
    /**********************************************************************************/
  });

  /* Basic setup to make Django and Angular play nice together */
  /* --------------------------------------------------------- */

  // Make sure angular understands Django's CSRF tokens
  meubisApp.config(['$httpProvider', function($httpProvider) {
      $httpProvider.defaults.headers.common['X-Requested-With'] = 'XMLHttpRequest';
      $httpProvider.defaults.xsrfCookieName = 'csrftoken';
      $httpProvider.defaults.xsrfHeaderName = 'X-CSRFToken';
  }]);

  // Change Angular's default start/end symbols, since they collide with Django's
  meubisApp.config(['$interpolateProvider', function($interpolateProvider) {
      $interpolateProvider.startSymbol('[[').endSymbol(']]');
  }]);

  // Don't strip trailing slashes from calculated URLs
  meubisApp.config(['$resourceProvider', function($resourceProvider) {
      $resourceProvider.defaults.stripTrailingSlashes = false;
  }]);
  /* --------------------------------------------------------- */

  /* App-wide settings --------------------------------------- */
  // location.origin holds the current base url, for example: https://jackopaw.com
  if (!location.origin)
     location.origin = location.protocol + "//" + location.host;
  /* --------------------------------------------------------- */

})();

