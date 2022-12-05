package Week2;
 

import java.util.Arrays;


class Colorspace {

    static float[] RGBtoCMY(float r, float g, float b) {
        //als je van rgb naar cmy wilt moet je eerst van 255 naar 0/1 berekenen omdat rgb meestal werkt van 0 tot 255 dus als we met een voorbeeld blauw op 200 zetten
        // moeten we 1 - (200/255)
        // vandaar de cormule y= 1-b ( het is niet delen door 255 aangezien in de vraag staat dat onze rgb waarden zoizo al van 0 tot 1 gaan)

        //berekeningen
        float c = (1 - r);
        float m = (1 - g);
        float y = (1 - b);

        //returnt de waardes die net zijn berekend
        return new float[] {c, m, y};
    }

    static float[] CMYtoRGB(float c, float m, float y) {
        //als je van rgb naar cmy gaat deet je 1-r maar nu wil je van cmy naar rgb dus doe je r= 1 - c 

        //berekeningen
        float r = (1 - c);
        float g = (1 - m);
        float b = (1 - y);

        //returned de berekende waardes
        return new float[] {r, g, b};
    }


   static float[] RGBtoHSL(float r, float g, float b) {
        //voor meer informatie over de formule gebruikt https://www.niwa.nu/2013/05/math-behind-colorspace-conversions-rgb-hsl/

        //pakt van de waardes gegeven het hoogste en laagste nummer bij math.max bijvoorbeeld waardes 8 9 4 dan word bij max nummer 9 gebruikt 
        float M = Math.max(r, Math.max(g, b));
        float m = Math.min(r, Math.min(g, b));

        //initialiseerd floats s en H
        float s = 0;
        float H = 0;

        //berekend gemiddelde van de waardes
        float l = ((M + m)/2);

        //beijkt of het gemiddelde lager of gelijk is aan 0.5 als dat zo is voerd hij de formule uit 
        if(l <= 0.5 ) {
           float S = (M - m ) / (M + m);
           s=S;

        }
        //bekijkt of het gemiddelde groter is dan 0.5 en voerd dan de forume uit
        if(l > 0.5 ) {
           float S = (M - m ) / (2 - M + m);
           s=S;
        }
     
        

        // If Red is max, then Hue = (G-B)/(max-min)
        // If Green is max, then Hue = 2.0 + (B-R)/(max-min)
        // If Blue is max, then Hue = 4.0 + (R-G)/(max-min)
        

        //als rood het hoogste is dan word het g-b / max - min
        //als groen het hoogste is dan word  het 2 + b - r / max - min
        //als blouw het hooste is word het 4 + r-g / max - min
        
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
   //forumle van b 
   static float B(float h, float cmin, float cmax){
    //voor meer informatie berekend het documentje in de vraag
    //als h kleiner dan 0 is telt hij er 360 bij op (zodat er geen fouten in het programma kan ontstaan)
    while (h < 0){
        h += 360.0f;
    }
    //berekend de modulo door h % 360 te doen he tis 
    float modulo = h % 360  ;

    //controleerd hoe groot de modulo is als 
    if (modulo < 120) {
        return cmin;
        //returned cmin
    }
    else if (modulo >= 120 && modulo < 180 ) {
        return cmin + (cmax - cmin) * (modulo - 120) / 60;
        //returned getal berekend in formule
    }
    else if (modulo >= 180 && modulo < 300 ) {
        return cmax;
        //returned cmin
    }
    else  {
        return cmax -(cmax-cmin) * (modulo - 300) / 60 ;
         //returned getal berekend in formule
    }
    }

   static float[] HSLtoRGB(float h, float s, float l) {
  
    //berekend cmin formule staat in bestandje in vraag
    float cmin = l + s * Math.abs(l - 0.5f) + (-0.5f*s);
    float cmax = l - s * Math.abs(l - 0.5f) + (0.5f*s);
    //roept functie B aan en vult daar parameters in 
    float b = B(h, cmin, cmax);
    float g = B(h + 120, cmin, cmax);
    float r = B(h - 120, cmin, cmax);


    
 
     
     
       return new float[] {r, g, b};
   }

   static float[] transparency(float r1, float g1, float b1, float alpha, float r2, float g2, float b2) {
       // hier word de transparency berekend formule staat in de slides
       float r = r1 * alpha + r2*(1-alpha);
       float g = g1 * alpha + g2*(1-alpha);
       float b = b1 * alpha + b2*(1-alpha);
       //returned r g en b
       return new float[] {r, g, b};
   }

   public static void main(String[] args) {
    // testcode
    // let op: de beoordeling wordt gedaan op basis van andere waarden
    System.out.println(Arrays.toString(RGBtoCMY(0.4f, 0.5f, 0.6f))); // (0.6, 0.5, 0.4)
    System.out.println(Arrays.toString(CMYtoRGB(0.4f, 0.5f, 0.6f))); // (0.6, 0.5, 0.4)
    System.out.println(Arrays.toString(RGBtoHSL(0.4f, 0.5f, 0.6f))); // (210.0, 0.2, 0.5)
    System.out.println(Arrays.toString(HSLtoRGB(100f, 0.5f, 0.6f))); // (0.533, 0.8, 0.4)
    System.out.println(Arrays.toString(transparency(0.4f, 0.5f, 0.6f, 0.7f, 0.8f, 0.9f, 1.0f))); // (0.52, 0.62, 0.72)
}
}