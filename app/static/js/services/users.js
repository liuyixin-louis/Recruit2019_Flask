

angular.module('userService', [])
	.factory('Users', ['$http', function($http) {
		return {
			create : function(userBody) {
				return $http.post('/api/users/add', userBody);
			}
		}
	}]);
