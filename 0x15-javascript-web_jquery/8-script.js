$.getJSON('https://swapi.co/api/films/?format=json', function (data) {
  $.each(data.results, function (index, element) {
    $('UL#list_movies').append('<li>' + element.title + '</li>');
  });
});
