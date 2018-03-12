$(document).ready(function () {
	$('#sidebarCollapse').on('click', function () {
		$('#sidebar').toggleClass('active');
	});
});

angular.module('myApp', []) // Specify the app to write for
	.controller('myCtrl', function($scope, $http) { // Specify the right controller
		$scope.productList = {} // Initialise the product list to be an empty dict

		$scope.getItems = function() {
			$http.get("http://localhost:5002/products").then(function (response) { // Run products.get() in api.py
				$scope.productList = response.data; // Take the response and set the product list to it
			});
		};

        $scope.addItem = function() {
            data = {ID: $scope.selected.ID, Category: $scope.selected.Category, Name: $scope.selected.Name,
            Quantity: $scope.selected.Quantity, Price: $scope.selected.Price, extrainfo: $scope.selected.extrainfo}
            // Gather all the given data into one dict
            $http.post("http://localhost:5002/products", data).then(function(response) {
                // post said data to this URL, the Products class
                $scope.getItems() // update the table
            });
        };

        $scope.delItem = function() {
            $http.delete("http://localhost:5002/product/" + $scope.selected, []).then(function(response) {
                $scope.getItems();
            });
        };

        $scope.selectItem = function(product) {
            $scope.selected = product;  // set whatever is passed in as the selected item
        };

//        $scope.newSearch = function(product) {
//            $scope.searchterm = {};
//        };

		$scope.getItems()
	});
