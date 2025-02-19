let url = 'https://swapi-api.alx-tools.com/api/films/?format=json';
$.get(url, function (data) {
  for (var film of data.results) {
    $('ul#list_movies').append(`<li>${film.title}</li>`);
  }
});
