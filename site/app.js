$(document).ready(function () {
	$('#sidebarCollapse').on('click', function () {
		$('#sidebar').toggleClass('active');
	});
});

angular.module('myApp', [])
	.controller('myCtrl', function($scope, $http) {
		$scope.productList = {}
		
		$scope.getItems = function() {
			$http.get("http://localhost:5002/products").then(function (response) {
				$scope.productList = response.data;
			});
		};
	});