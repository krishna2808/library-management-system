

$(document).ready(function() {
	$("#sign-up-submit").click(function() {
		var payload = {
			"email": $("#sign-up-email").val(),
			"username": $("#sign-up-username").val(),
			"password": $("#sign-up-password").val(),
		}
		debugger
		$.ajax({
			url: 'http://localhost:8000/account/signup/',
			type: 'POST', 
			data: payload,
			dataType: 'json',
			success: function(data) {
				console.log('AJAX call successful:', data);
				$(".msg").show();
				$("#sign-up-email").val("")
                $("#sign-up-username").val("")
				$("#sign-up-password").val("")

			},
			error: function(xhr, status, error) {
				console.log(xhr)
				console.error('AJAX call failed:', status, error);
			}
		});
	});







	$("#sign-in-submit").click(function() {
		var payload = {
			"email": $("#sign-in-email").val(),
			"password": $("#sign-in-password").val(),
		}
		debugger
		$.ajax({
			url: 'http://localhost:8000/account/signin/',
			type: 'POST', 
			data: payload,
			dataType: 'json',
			success: function(data) {
				localStorage.setItem("access_token", data.access);
				localStorage.setItem("refresh_token", data.refresh);
				console.log('AJAX call successful:', data);
				window.location.href = window.location.origin + "/lms/dashboard"
			},
			error: function(xhr, status, error) {
				console.log(xhr)
				console.error('AJAX call failed:', status, error);
			}
		});
	});










});

