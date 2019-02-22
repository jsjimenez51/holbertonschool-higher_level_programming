$.ajax({
  type: 'GET',
  url: 'https://fourtonfish.com/hellosalut/?lang=fr',
  dataType: 'json',
  success: function (data) {
    let bonjour = 'hello';
    if ($('HTML')[0].lang === 'fr') {
      bonjour = data.hello;
    }
    $('DIV#hello').text(bonjour);
  }
});
