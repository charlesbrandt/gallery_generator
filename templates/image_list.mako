<h3>${title}</h3>

Images are clickable...
<div class="images">
% for image in images:
<div class="image">
  ##<span class="image"> <a href="${image.path.to_relative(extension='.html')}" alt="Image on ${str(image.timestamp())}"><img src="${image.get_size('small', relative=True)}" /></a></span>
  <span class="image"> <a href="${image.path.to_relative(extension='.html')}" alt="Image on ${str(image.timestamp())}"><img class="small" src="${image.size_path('small').to_relative()}" /></a></span>
</div>
% endfor

<div class="row"></div>

</div>
