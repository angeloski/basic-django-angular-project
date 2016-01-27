(function(){
 
  angular.module('meubisApp').factory('ProductsListFactory',[
            '$http', 
    function($http) {
      var ProductsListFactory = function() {
        this.items = [];
        this.busy = false;
        this.show_loading = false;
        this.limit = 100;
        this.first_id = 0;
        this.last_id = 0;
      };

      ProductsListFactory.prototype.fetchProducts = function() {

        if (this.busy) return;
        this.busy = true;
        
        var get_products_list_url = location.origin+'/api/products/products/';

        $http.get(get_products_list_url)
            .success(function(products_feed) {
                for (var i = 0; i < products_feed.results.length; i++) {
                    this.items.push(products_feed.results[i]);
                }
                if (products_feed.results.length != 0){
                    this.show_loading = true;
                }else {
                    this.show_loading = false;
                }  
                this.busy = false;
            }
            .bind(this));
      };
      return ProductsListFactory;
    }]);

}());


