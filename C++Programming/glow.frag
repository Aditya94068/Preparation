// glow.frag - Bloom/Glow shader for SFML 3.0
#version 120

uniform sampler2D texture;
uniform vec4 glowColor;
uniform float glowRadius;

void main() {
    vec2 coord = gl_TexCoord[0].xy;
    vec2 center = vec2(0.5, 0.5);
    float dist = distance(coord, center);
    
    // Smoothly calculate glow based on distance
    float glow = 1.0 - smoothstep(0.0, glowRadius, dist);
    
    // Sample texture color
    vec4 color = texture2D(texture, coord);
    
    // Blend final pixel color with glow color
    gl_FragColor = color + vec4(glowColor.rgb, glowColor.a * glow);
}