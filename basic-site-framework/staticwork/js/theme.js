
function Jumbotron() {
    var elements = [];

    function Jumbotron() {
        elements = jQuery('.jumbotron').toArray();
    }

    this.slide_left = function(index) {
        jQuery(elements[index]).animate({
            left: -window.innerWidth
        }, 1000);
    };

    this.move_to_right = function(index) {
        jQuery(elements[index]).css({
            left: window.innerWidth
        });
    };

    Jumbotron();

}
var j;
window.addEventListener('load', function(){
    j = new Jumbotron();
});
