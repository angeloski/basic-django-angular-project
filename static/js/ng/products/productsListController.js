(function(){
 
angular.module('meubisApp').controller('ProductsListController', [
          '$scope', '$rootScope', '$modal', '$log', '$http', '$timeout', '$filter', 'ProductsListFactory',
  function ($scope, $rootScope, $modal, $log, $http, $timeout, $filter, ProductsListFactory) {

    $scope.sortType     = 'updated_at'; // set the default sort type
    $scope.sortReverse  = false;  // set the default sort order
    $scope.searchProduct   = '';     // set the default search/filter term

    $rootScope.productsListFactory = new ProductsListFactory();
    $rootScope.productsListFactory.fetchProducts();

    /**********************************************************************************/


  }]);

}());