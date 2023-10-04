$.ajax({
  type: 'GET',
  url: 'https://swapi-api.alx-tools.com/api/films/?format=json',
  success: function (data) {
    $.each(data.results, function (i, result) {
      $('UL#list_movies').append('\n<li>' + result.title + '</li>');
    }
    );
  }
}
);
