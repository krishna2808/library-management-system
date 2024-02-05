

// Define the requestBook function outside the document ready block
function requestBook(book_id) {
	var header = {
		"Authorization": "Bearer " + localStorage.getItem("access_token")
	}
	var now = new Date();
	var formattedNow = now.toISOString().slice(0, 16);
    console.log('book data', book_id);
    var cardsContainer = $('#dashboard-book');

    function createCardForm() {
        var formHtml = `
            <form id="addCardForm">
                <label for="book-id">Book ID:</label>
                <input type="text" id="book-id" value=${book_id} name="book-id" required disabled>
                
				<label for="book-issue-date">Book Issue Date:</label>
                <input type="datetime-local" id="book-issue-date" name="book-issue-date" required min=${formattedNow} >

                <label for="book-due-date">Book Due Date :</label>
                <input type="datetime-local" id="book-due-date" name="book-due-date" required min=${formattedNow}>

                <button type="submit">Submit</button>
                <button type="button" id="cancelButton">Cancel</button>
            </form>
        `;
        
        cardsContainer.append(formHtml);

        $('#addCardForm').submit(function (event) {
            event.preventDefault();
            payload = {
			    'book_id' : $("#book-id").val(),
				"issue_datetime" : $("#book-issue-date").val(),
				"return_datetime" : $("#book-due-date").val()
			}

			$.ajax({
				url: 'http://localhost:8000/lms/user-book-request/',
				type: 'POST',
				data : payload,
				headers: header,
				dataType: 'json',
				success: function (data) {
					console.log('AJAX call successful:', data);
					book_data = data;
				},
				error: function (xhr, status, error) {
					console.log(xhr);
					// window.location.href = window.location.origin + "/account/";
					console.error('AJAX call failed:', status, error);
				}
			});
		


            $('#addCardForm').remove();
        });

        $('#cancelButton').click(function () {
            $('#addCardForm').remove();
        });
    }

    // Create a form for adding a card
    createCardForm();

    $.ajax({
        url: 'http://localhost:8000/lms/book/',
        type: 'GET',
        headers: header,
        dataType: 'json',
        success: function (data) {
            console.log('AJAX call successful:', data);
            book_data = data;
        },
        error: function (xhr, status, error) {
            console.log(xhr);
            window.location.href = window.location.origin + "/account/";
            console.error('AJAX call failed:', status, error);
        }
    });
}




$(document).ready(function() {
	var header = {
		"Authorization": "Bearer " + localStorage.getItem("access_token")
	}
    var book_data = ''
	$.ajax({
		url: 'http://localhost:8000/lms/book/',
		type: 'GET', 
		headers: header,
		dataType: 'json',
		success: function(data) {
			console.log('AJAX call successful:', data);
			book_data = data

            var dashboard = $("#dashboard-book");

			function createBookCard(book) {
				// Create HTML card for the book
				var cardHtml = `
					<div key=${book.id} class="col">
						<div class="card">
							<img src="${book.image}" class="card-img-top cart-image" alt="${book.title}" />
							<div class="card-body">
								<h5 class="card-title">${book.title}</h5>
								<p class="card-text">${book.description}</p>
								<button  class="btn btn-primary"  onclick="requestBook(${book.id})" > Request Book</button> &nbsp;&nbsp;&nbsp;
							</div>
			
						</div>
			
					</div>
				`;
	
				// Append the card to the container
				dashboard.append(cardHtml);
			}
	
			// Iterate over each book and create a card for it
			data.forEach(function(book) {
				createBookCard(book);
			});




			
			
		},
		error: function(xhr, status, error) {
			console.log(xhr)
			window.location.href = window.location.origin + "/account/"
			console.error('AJAX call failed:', status, error);
		}
	});




});
