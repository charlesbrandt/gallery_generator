<div class="row">

  <span id="maincolumn"> 
    % if n:
    <a href="${n.path.to_relative(extension='.html')}" alt="previous" accesskey="d">
      <img class="pic" width="${size}" src="${image.size_path('large', square=False).to_relative()}" alt="Image on ${str(image.timestamp())}">
    </a>
    % else: 
    <img class="pic" width="${size}" src="${image.size_path('large', square=False).to_relative()}" alt="Image on ${str(image.timestamp())}">
    % endif
  </span>

  <span id="sidebar">
    <a href="index.html" alt="album">
      <img width="50" src="/img/up.svg">
    </a> <br />

    % if p:
    <a href="${p.path.to_relative(extension='.html')}" alt="previous" accesskey="a">
      <img width="50" src="/img/left.svg">
    </a> 
    % else: 
      <img width="50" style="opacity:.2" src="/img/left.svg">
    % endif
&nbsp;
&nbsp;
&nbsp;
&nbsp;
    % if n:
    <a href="${n.path.to_relative(extension='.html')}" alt="next" accesskey="d">
      <img width="50" src="/img/right.svg">
    </a> <br />
    % else: 
      <img width="50" style="opacity:.2" src="/img/right.svg">
      <br />
    % endif


    % for prev in prevs:
    <a href="${prev.path.to_relative(extension='.html')}" alt="previous">
      <img class="tiny" src="${prev.size_path('tiny').to_relative()}" alt="Image on ${str(prev.timestamp())}">
    </a> <br />
    % endfor

<hr>

    % for item in nexts:
    <a href="${item.path.to_relative(extension='.html')}" alt="previous">
       <img class="tiny" src="${item.size_path('tiny').to_relative()}" alt="Image on ${str(item.timestamp())}">
    </a> <br />
    % endfor
    
    <a href="${image.path.to_relative()}" alt="full size link" class="full_res">Full Resolution</a> <br />

  </span>

</div>
<div class="row"></div>
