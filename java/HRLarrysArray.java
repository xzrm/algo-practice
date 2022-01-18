import java.util.ArrayList;
import java.util.Arrays;
import java.util.Collections;
import java.util.List;
import java.util.Optional;
import java.util.stream.Collectors;
import java.util.stream.IntStream;
import java.util.stream.Stream;

//The code does the check if sorting is possible but in the current implementation it times out
class HRLarrysArray {
    public static List<Integer> rotate(List<Integer> arr) {
        int len = 3;
        return IntStream.range(0, len)
                .map(i -> arr.get((i + 1) % 3))
                .boxed().collect(Collectors.toList());
    }

    public static Optional<List<Integer>> getSubList(List<Integer> arr, Integer val) {
        return IntStream.range(0, arr.size() - 2)
                .mapToObj(i -> arr.subList(i, i + 3))
                .filter(s -> s.contains(val)).findFirst();
    }

    public static void main(String[] args) {
        String s = "424 183 20 527 911 603 589 707 78 728 905 598 805 587 132 770 122 354 688 543 802 936 77 320 738 594 764 69 620 567 564 4 213 704 590 49 451 355 147 163 932 569 493 780 846 812 511 626 640 22 2 44 878 924 299 693 499 242 51 127 33 225 400 455 218 216 852 779 309 546 30 310 120 160 651 287 926 324 749 177 956 130 194 768 40 602 165 322 818 709 351 375 209 659 422 760 792 553 525 250 650 705 100 748 916 762 369 530 278 178 175 824 336 427 933 736 690 864 934 685 631 815 156 79 757 215 902 64 808 350 113 202 667 265 537 61 888 953 276 101 384 830 85 955 105 170 391 584 234 689 372 613 920 744 389 109 371 895 751 944 301 526 880 618 807 630 954 58 838 224 865 829 879 497 809 574 778 423 217 205 958 703 116 313 740 540 348 763 535 311 539 334 153 27 890 306 562 475 520 8 437 903 882 129 701 628 316 88 833 222 831 578 950 860 406 146 835 877 295 549 702 548 896 332 502 585 929 822 269 66 899 140 907 13 922 281 233 340 373 694 446 836 560 42 691 586 771 572 554 223 862 600 573 396 538 199 869 243 426 665 83 378 746 479 231 948 854 68 413 441 782 883 238 158 655 868 292 621 198 500 186 57 323 14 159 359 797 118 832 555 274 99 492 32 139 55 848 551 576 556 151 853 583 241 734 756 377 558 471 468 52 343 366 203 927 939 421 448 487 919 804 221 682 732 580 800 169 521 232 623 208 837 15 328 341 827 230 561 851 870 716 461 356 275 592 54 284 937 627 125 35 1 410 741 21 512 103 636 219 327 337 872 605 753 731 519 643 508 887 697 319 228 910 173 333 912 344 142 29 711 773 949 646 908 261 143 415 184 663 610 435 473 53 857 70 254 407 735 296 244 649 115 498 507 671 604 957 672 660 657 379 91 632 240 106 575 593 816 349 60 673 104 457 947 315 249 796 220 124 821 945 393 565 409 524 48 843 545 532 181 149 828 677 6 700 817 92 416 789 214 308 695 190 270 398 834 477 345 31 399 900 376 941 300 795 515 683 417 898 280 367 258 617 381 669 368 588 884 767 200 453 290 715 110 544 607 712 820 444 395 197 17 644 787 645 599 595 529 727 75 826 414 80 547 259 472 257 766 874 252 440 397 227 528 889 678 875 411 347 534 450 361 661 501 566 904 201 810 267 382 425 943 674 279 251 434 326 662 449 648 342 931 582 148 656 285 137 387 207 772 62 488 577 518 730 906 743 331 12 34 494 41 478 611 893 403 273 459 266 338 608 141 476 486 383 318 483 871 811 138 402 951 861 74 166 930 579 597 405 150 168 717 606 438 850 268 609 721 642 454 485 134 404 917 65 38 724 302 418 144 710 866 794 235 188 43 329 886 206 786 681 294 192 517 523 123 652 286 692 952 76 699 723 89 614 516 39 654 633 363 839 855 380 283 325 237 94 210 819 876 439 352 98 881 271 253 412 330 447 915 262 465 152 167 462 131 204 698 346 897 719 722 182 256 601 541 408 940 452 679 666 212 464 97 737 776 362 445 50 161 388 293 84 312 739 365 357 777 946 59 490 45 859 429 670 196 174 72 36 9 510 806 658 305 729 708 482 436 668 73 358 303 470 484 255 96 552 591 432 474 894 272 504 480 639 282 758 297 246 87 185 443 16 239 63 867 790 5 489 191 959 913 263 570 513 842 245 189 19 401 390 67 458 840 370 785 522 629 844 928 765 229 481 430 798 164 107 24 634 638 195 112 82 761 823 892 863 18 126 247 102 304 10 788 289 885 783 37 680 714 803 769 873 901 456 496 93 622 624 747 696 176 637 419 825 925 542 909 849 918 119 706 317 420 121 431 612 442 47 145 353 725 7 56 385 726 392 162 95 563 938 321 179 46 891 248 117 172 495 277 750 755 921 469 154 841 581 364 718 923 128 335 133 742 531 505 559 935 211 86 26 653 813 288 858 433 394 664 171 684 619 675 90 550 733 533 647 81 460 466 260 71 157 536 360 960 193 314 615 641 386 187 135 774 793 720 226 814 759 291 467 374 571 686 713 914 503 775 847 180 791 506 298 111 942 3 801 339 754 114 155 596 845 25 264 799 752 463 557 784 616 568 635 108 236 509 781 23 687 28 514 856 491 676 745 136 307 11 428 625";
        // String s = "1 6 5 2 4 3";
        List<Integer> arr = Arrays.stream(s.split(" ")).map(Integer::parseInt).collect(Collectors.toList());
        System.out.println(larrysArray(arr));

    }

    public static String larrysArray(List<Integer> arr) {
        ArrayList<Integer> toValidate = new ArrayList<>(arr);
        Collections.sort(toValidate);

        for (int i = 0; i < arr.size(); i++) {
            int currentInt = i + 1;
            if (currentInt == arr.get(i)) {
                continue;
            }
            List<Integer> unsortedSubList = arr.subList(i, arr.size());
            if (unsortedSubList.size() < 3) {
                return "NO";
            }
            Integer minVal = Collections.min(unsortedSubList);
            while (!unsortedSubList.get(0).equals(minVal)) {
                List<Integer> subList = getSubList(unsortedSubList, currentInt).get();
                // to locate the subList within the unsortedSubList
                int index = unsortedSubList.indexOf(subList.get(0));
                while (!subList.get(0).equals(minVal)) {
                    subList = rotate(subList);
                }
                for (int j = 0; j < 3; j++) {
                    unsortedSubList.set(index + j, subList.get(j));
                }
            }
            arr = Stream.concat(arr.subList(0, i)
                    .stream(), unsortedSubList.stream())
                    .collect(Collectors.toList());

            if (toValidate.equals(arr)) {
                return "YES";
            }
        }
        if (toValidate.equals(arr)) {
            return "YES";
        }
        return "NO";
    }
}