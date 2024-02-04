

export function isAuthentication(){

    var isAuthorize = false
	var header = {
		"Authorization": "Bearer " + localStorage.getItem("access_token")
	}
	debugger
	$.ajax({
		url: 'http://localhost:8000/account/signup/',
		type: 'POST', 
		data: payload,
		dataType: 'json',
		headers: header,
		success: function(data) {
			console.log('AJAX call successful:', data);
			isAuthorize = true
		},
		error: function(xhr, status, error) {
			console.log(xhr)
			window.location.href = window.location.origin + "/account/"
			console.error('AJAX call failed:', status, error);
			isAuthorize = false
		}
	});

    return isAuthorize


}