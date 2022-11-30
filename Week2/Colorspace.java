package Week2;
 

import java.util.Arrays;


class Colorspace {

    static float[] RGBtoCMY(float r, float g, float b) {
        // to do

        float c = (1 - r);
        float m = (1 - g);
        float y = (1 - b);

        return new float[] {c, m, y};
    }

   static float[] CMYtoRGB(float c, float m, float y) {
    float r = (1 - c);
    float g = (1 - m);
    float b = (1 - y);

        // to do
       return new float[] {r, g, b};
    }
//
   static float[] RGBtoHSL(float r, float g, float b) {
        // to do
        float M = Math.max(r, Math.max(g, b));
        float m = Math.min(r, Math.min(g, b));
        float s = 0;
        float H = 0;

        float d = (M-m);

        float l = ((M + m)/2);

        if(l <= 0.5 ) {
           float S = (M - m ) / (M + m);
           s=S;

        }
        if(l > 0.5 ) {
           float S = (M - m ) / (2 - M + m);
           s=S;
        }
     
        

        // If Red is max, then Hue = (G-B)/(max-min)
        // If Green is max, then Hue = 2.0 + (B-R)/(max-min)
        // If Blue is max, then Hue = 4.0 + (R-G)/(max-min)

        if ( r == M) {
        H = (g-b)/(M-m);
        }
        if ( g == M) {
        H = 2 + (b - r)/(M - m);
        }
        if ( b == M) {
        H = 4 + (r - g) / (M - m);
        }
        float h = H * 60;
        


        
        return new float[] {h, s, l};
   }

   static float[] HSLtoRGB(float h, float s, float l) {
    float b= 0;
    float getal1 =  l - 0.5f;

    float getal2 = Math.abs(getal1);

    float cmin =(l + s) + getal2 - (0.5f*s);
    float cmax =(l + s) + getal2 + (0.5f*s);
    float modulo = h % 360;
    if (modulo < 120) {
        b = cmin;
    }
    if (modulo >= 120 || modulo < 180 ) {
        b = cmin + (cmax - cmin) * (h % (360 - 120) / 60);
    }
    if (modulo >= 180 || modulo < 300 ) {
        b = cmax;
    }
    if (modulo >= 300 || modulo < 360 ) {
        b = cmax -(cmax-cmin) * (h % (360 - 300) / 60 );
    }
 
    
    float g = b * (h + 120);
    float r = b * (h - 120);


    
 
     
     
       return new float[] {r, g, b};
   }






   static float[] transparency(float r1, float g1, float b1, float alpha, float r2, float g2, float b2) {
       // to do
       float r = r1 * alpha + r2*(1-alpha);
       float g = g1 * alpha + g2*(1-alpha);
       float b = b1 * alpha + b2*(1-alpha);
       return new float[] {r, g, b};
   }

    public static void main(String[] args) {
        // testcode
        // let op: de beoordeling wordt gedaan op basis van andere waarden
        //System.out.println(Arrays.toString(RGBtoCMY(0.4f, 0.5f, 0.6f))); // (0.6, 0.5, 0.4)
        //System.out.println(Arrays.toString(CMYtoRGB(0.4f, 0.5f, 0.6f))); // (0.6, 0.5, 0.4)
 //      System.out.println(Arrays.toString(RGBtoHSL(0.4f, 0.5f, 0.6f))); // (210.0, 0.2, 0.5)
     System.out.println(Arrays.toString(HSLtoRGB(100f, 0.5f, 0.6f))); // (0.533, 0.8, 0.4)
    // System.out.println(Arrays.toString(transparency(0.4f, 0.5f, 0.6f, 0.7f, 0.8f, 0.9f, 1.0f))); // (0.52, 0.62, 0.72)/
    }
}