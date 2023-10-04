document.addEventListener('DOMContentLoaded', () => {
  $('DIV#add_item').click(function () {
    $('UL.my_list').append('\n<li>Item</li>');
  });

  $('DIV#remove_item').click(function () {
    $('UL.my_list').find('li').slice(-1).remove();
  });

  $('DIV#clear_list').click(function () {
    $('UL.my_list').empty();
  });
});
