angular.module('userController', [])
	.controller('mainController', ['$scope', 'Users', function($scope, Users) {

		$scope.userBody = {};

		$scope.enroll = function() {
			let msg = JSON.stringify($scope.userBody);
			console.log("前端上传：\n" + msg);
			// console.log($scope.userBody);

			Users.create($scope.userBody);

			alert("您已成功报名！");
		};

	}]);
