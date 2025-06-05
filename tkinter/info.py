# pre_processed_images = ['emirates-777x.jpg', 'dc-10.jpg', '787-dreamliner.jpg', 'e175.jpg', 'a380.jpg', 'kc-46-pegasus.jpg', 'c-130-hercules.jpg', 'c17-globemaster.jpg', '737-max.jpg', 'a319.jpg']

pre_processed_images = ['https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcRvYe-DhXayITOnzaMkc_3G3I-6J4iYLSIkPg&s', 
                        'https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcTCgZkjJhWHzvxLLXsfrsqY0Ffkx-wagwbj3w&s',
                        'https://upload.wikimedia.org/wikipedia/commons/4/4e/Boeing_787_N1015B_ANA_Airlines_%2827611880663%29_%28cropped%29.jpg',
                        'https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcTewok5CBSfkYZN7QQGmdRPLj_CqU8uNx1xDA&s',
                        'https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcRe2FC5CuEkgw01uIbZwCOny5EDYNzrYEqfHA&s',
                        'https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcS5AN139O9eb6Yj5d7kwAdZjo9VHD6xq4efdg&s',
                        'https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcSwvsvDOaCUGMI_tyctoH1RNd27ERC9n5kPSg&s',
                        'https://upload.wikimedia.org/wikipedia/commons/b/bc/C-17_test_sortie.jpg',
                        'https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcQMfgBXW8yG_1gIckNEgXM3jSx8uomH9jP8CQ&s',
                        'https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcStcjP38h5GQDQ9OCgRxREM2d7UyxMEQLiNuQ&s'
]

labels = [
    [['boeing 777x', 'boeing 777', '777', '777x'], ['mcdonnell douglas dc10', 'md dc10','dc10']], 
    [['boeing 7879 dreamliner', 'boeing 787 dreamliner', '7879', '787'], ['embraer 175', 'embraer e175', 'e175']], 
    [['airbus a380', 'a380'], ['boeing kc46 pegasus', 'boeing kc46', 'kc46 pegasus', 'pegasus', 'kc46']], 
    [['lockheed martin c130j super hercules', 'lockheed martin c130 hercules', 'lockheed martin c130', 'c130 hercules', 'lm c130' ,'c130'], ['boeing c17 globemaster', 'boeing c17', 'c17 globemaster', 'c17']],
    [['boeing 737 max 9', 'boeing 737 max', 'boeing 737', '737 max', '737'],['airbus a319', 'a319']]
]