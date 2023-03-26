load chestVolume
whos
V = im2single(V);

for z = 1:318
    XY = V(:,:,z);
    %imageSegmenter(XY);
    BW = XY > 0.5098;
    BW = imcomplement(BW);
    BW = imclearborder(BW);
    BW = imfill(BW, "holes");
    radius = 3;
    decomposition = 0;
    se = strel("disk",radius,decomposition);
    BW = imerode(BW, se);
    maskedImageXY = XY;
    maskedImageXY(~BW) = 0;
    imwrite(maskedImageXY, string(z) + ".png");
    fprintf(string(z));
end