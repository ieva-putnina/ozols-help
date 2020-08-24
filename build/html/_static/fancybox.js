  <script type="text/javascript">
    $(function(){
      $('.image-reference').fancybox({
        // API options
        afterShow: function () {
            $(".fancybox-image")
            // second method
            .on("click", function () {
                $.fancybox.close(true);
            });
        }
    });
    })
  </script>
