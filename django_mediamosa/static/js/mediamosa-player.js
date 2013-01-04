$(document).ready(function() {

    // looks for mediamosa classes and activates the player
    $('span.mediamosa').each(function(index) {
        var asset_id = $(this).data('asset');
        var mediafile_id = $(this).data('mediafile');

        // query django-mediamosa for the player code
        $.ajax({
            url: "/mediamosa/assets/" + asset_id
                 + "/mediafiles/" + mediafile_id + "/play",
            context: $(this)
        }).done(function(data) {
            $(this).html(data);
        });
    });

})