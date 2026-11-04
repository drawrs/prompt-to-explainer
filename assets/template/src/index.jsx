import React from 'react';
import {AbsoluteFill, Composition, interpolate, registerRoot, useCurrentFrame} from 'remotion';

function Film() {
  const frame = useCurrentFrame();
  const opacity = interpolate(frame, [0, 14], [0, 1], {extrapolateRight: 'clamp'});
  return <AbsoluteFill style={{background: '#101210', color: '#e7e4da', justifyContent: 'center', alignItems: 'center', font: '52px sans-serif'}}>
    <div style={{opacity}}>Field notes</div>
  </AbsoluteFill>;
}

function Root() {
  return <Composition id="Film" component={Film} width={720} height={1280} fps={30} durationInFrames={900}/>;
}
registerRoot(Root);
