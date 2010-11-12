django.jQuery(document).ready(function() {
    if (window.top != window) {
        
        images = django.jQuery('img');
        
        images.css('cursor', 'pointer');
        
        images.click(function(){
            
            var win = tinyMCEPopup.getWindowArg('window');
            
            var doc = win.document;
            
            var image = django.jQuery(this);
            
            var url = image.attr('src');
            var alt = image.attr('alt');
            
            var id = tinyMCEPopup.getWindowArg('input');
            
            django.jQuery('#' + id, doc).val(url);
            django.jQuery('#alt', doc).val(alt);

            if (typeof(win.ImageDialog) != "undefined") {
                if (win.ImageDialog.getImageData) win.ImageDialog.getImageData();
                if (win.ImageDialog.showPreviewImage) win.ImageDialog.showPreviewImage(url);
            }

            tinyMCEPopup.close();
            return false;
        });
        
        /*$('#changelist tbody a.image-picker').click(function(e) {
            var url = $(this).attr('href');
            var win = tinyMCEPopup.getWindowArg("window");
            var alt = $(this).find('img').attr('alt');

            win.document.getElementById(tinyMCEPopup.getWindowArg("input")).value = url;
            win.document.getElementById('alt').value = alt;

            if (typeof(win.ImageDialog) != "undefined") {
                if (win.ImageDialog.getImageData) win.ImageDialog.getImageData();
                if (win.ImageDialog.showPreviewImage) win.ImageDialog.showPreviewImage(url);
            }

            tinyMCEPopup.close();
            return false;
        });*/
        
        /*
         $().ready(function() {
            if (window.parent) {
                $.getscript('/media/lib/tiny_mce/tiny_mce_popup.js', function() {
                    $('#changelist tbody a.image-picker').click(function(e) {
                        var url = $(this).attr('href');
                        var win = tinyMCEPopup.getWindowArg("window");
                        var alt = $(this).find('img').attr('alt');
        
                        win.document.getElementById(tinyMCEPopup.getWindowArg("input")).value = url;
                        win.document.getElementById('alt').value = alt;
        
                        if (typeof(win.ImageDialog) != "undefined") {
                            if (win.ImageDialog.getImageData) win.ImageDialog.getImageData();
                            if (win.ImageDialog.showPreviewImage) win.ImageDialog.showPreviewImage(url);
                        }
        
                        tinyMCEPopup.close();
                        return false;
                    });
                });
            }
        });
        */
    }
});