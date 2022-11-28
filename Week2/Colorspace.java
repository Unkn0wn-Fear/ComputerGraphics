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
//    static float[] RGBtoHSL(float r, float g, float b) {
//        // to do
//        return new float[] {h, s, l};
//    }
//
//    static float[] HSLtoRGB(float h, float s, float l) {
//        // to do
//        return new float[] {r, g, b};
//    }
//
//    static float[] transparency(float r1, float g1, float b1, float alpha, float r2, float g2, float b2) {
//        // to do
//        return new float[] {r, g, b};
//    }

    public static void main(String[] args) {
        // testcode
        // let op: de beoordeling wordt gedaan op basis van andere waarden
        System.out.println(Arrays.toString(RGBtoCMY(0.4f, 0.5f, 0.6f))); // (0.6, 0.5, 0.4)
        System.out.println(Arrays.toString(CMYtoRGB(0.4f, 0.5f, 0.6f))); // (0.6, 0.5, 0.4)
//        System.out.println(Arrays.toString(RGBtoHSL(0.4f, 0.5f, 0.6f))); // (210.0, 0.2, 0.5)
//        System.out.println(Arrays.toString(HSLtoRGB(100f, 0.5f, 0.6f))); // (0.533, 0.8, 0.4)
//        System.out.println(Arrays.toString(transparency(0.4f, 0.5f, 0.6f, 0.7f, 0.8f, 0.9f, 1.0f))); // (0.52, 0.62, 0.72)/
    }
}