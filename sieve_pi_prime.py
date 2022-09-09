from manim import *

class pi_prime_product(Scene):
    def construct(self):
        #self.next_section("Sieve of Eratosthenes", skip_animations=True)
        ##1. Entrance of the numbers
        #m
        vg = 12*18
        vn = 12*9
        gg = VGroup(*[Integer(g+2) for g in range(vg)])
        gg.arrange_in_grid(rows=18, buff=0.45)
        gg.to_edge(UP, buff=1)
        v2 = list(range(2, vn, 2))
        v3 = [7,13,19,25,31,37,43,49,55,61,67,73,79,85,91,97,103]
        v5 = [23,33,53,63,83,93]
        v7 = [47,75,89]
        pg = SurroundingRectangle(gg[0], color=RED)
        #a
        self.play(ShowIncreasingSubsets(gg[0:vn]), run_time=4, rate_func=linear)
        #2. Erastostenes with 2
        self.play(Create(pg))
        self.play(
            AnimationGroup(*[gg[n].animate.set_color(RED) for n in v2]),
            run_time=2,
            )
        self.play(
            AnimationGroup(
                *[
                Succession(
                    Indicate(gg[n], color=RED, run_time = 1/(1+0.5*i)),
                    FadeOut(gg[n], shift=DOWN, run_time = 1/(1+0.5*i)),
                    )
                for n,i in zip(v2,range(len(v2)))
                ],
                lag_ratio = 1,
                )
            )
        self.wait(1)
        #3. Erastostenes with 3
        self.play(pg.animate.move_to(gg[1]))
        self.play(
            AnimationGroup(*[gg[n].animate.set_color(RED) for n in v3]),
            run_time=2,
            )
        self.play(
            AnimationGroup(
                *[
                Succession(
                    Indicate(gg[n], color=RED, run_time = 1/(1+0.5*i)),
                    FadeOut(gg[n], shift=DOWN, run_time = 1/(1+0.5*i)),
                    )
                for n,i in zip(v3,range(len(v3)))
                ],
                lag_ratio = 1,
                )
            )
        self.wait(1)
        #4. Erastostenes with 5
        self.play(pg.animate.move_to(gg[3]))
        self.play(
            AnimationGroup(*[gg[n].animate.set_color(RED) for n in v5]),
            run_time=2,
            )
        self.play(
            AnimationGroup(
                *[
                Succession(
                    Indicate(gg[n], color=RED),
                    FadeOut(gg[n], shift=DOWN),
                    )
                for n in v5
                ]
                )
            )
        self.wait(1)
        #5. Erastostenes with 7
        self.play(pg.animate.move_to(gg[5]))
        self.play(
            AnimationGroup(*[gg[n].animate.set_color(RED) for n in v7]),
            run_time=2,
            )
        self.play(
            AnimationGroup(
                *[
                Succession(
                    Indicate(gg[n], color=RED),
                    FadeOut(gg[n], shift=DOWN),
                    )
                for n in v7
                ]
                )
            )
        self.wait(1)
        #6.Zoom out!
        for n in range(vg):
            for i in range(2, n):
                if ((n+2)%i) == 0:
                    gg[n].set_opacity(0)
        gg[2].set_opacity(0)
        self.play(Uncreate(pg))
        self.play(
            gg.animate.scale(0.5).to_edge(UP, buff=1),
            rate_func=rate_functions.ease_in_out_sine,
            run_time=4,
            )
        self.wait(2)
        self.play(FadeOut(gg))
        self.wait(2)

        #self.next_section("Sum with 2", skip_animations=True)
        tz = TexTemplate()
        tz.add_to_preamble(r"\newcommand\z[1]{\frac{1}{#1^s}}")
        tz.add_to_preamble(r"\newcommand\zm[1]{\frac{1}{{#1^s} \times 2^s}}")
        l1 = Tex("Zeta function:").scale(1.25).to_corner(UL)
        t1 = MathTex(
            r"\zeta(s)=",
            "\\z{1}+","\\z{2}+","\\z{3}+","\\z{4}+","\\z{5}+","\\z{6}+","\\z{7}+",
            "\\z{8}+","\\z{9}+","\\cdots",
            tex_template=tz,
            ).scale(1.25).next_to(l1, DOWN, buff=0.5, aligned_edge=LEFT)
        to = Integer(1)
        t1[10].align_to(t1[8], LEFT)
        lm = MathTex("\\text{Multiply by }", "\\frac{1}{2^s}").set_color(RED)
        lm.scale(1.25).next_to(t1, DOWN, buff=1, aligned_edge=LEFT)
        tm = MathTex(
            r"\frac{1}{2^s}\zeta(s)=",
            "\\zm{1}+","\\zm{2}+","\\zm{3}+","\\zm{4}+","\\zm{5}+",
            tex_template=tz,
            ).scale(1.25).next_to(t1, DOWN, buff=1, aligned_edge=LEFT)
        tm[0][0:4].set_color(RED)
        for t in range(1,5):
            tm[t][5:7].set_color(RED)
        te = MathTex(
            r"\frac{1}{2^s}\zeta(s)=",
            "\\frac{1}{(1\\times 2)^s}+","\\frac{1}{(2\\times 2)^s}+","\\frac{1}{(3\\times 2)^s}+",
            "\\frac{1}{(4\\times 2)^s}+",
            ).scale(1.25).move_to(tm, aligned_edge=LEFT)
        te[0][0:4].set_color(RED)
        for t in range(1,5):
            te[t][2].set_color(RED)
        for t in range(1,5):
            te[t][5:8].set_color(RED)
        t2 = MathTex(
            r"\frac{1}{2^s}\zeta(s)=",
            "\\z{2}+","\\z{4}+","\\z{6}+","\\z{8}+","\\z{10}+","\\z{12}+","\\z{14}+",
            "\\cdots",
            tex_template=tz,
            ).scale(1.25).move_to(tm, aligned_edge=LEFT)
        t2.set_color(RED)
        t2[0][4:8].set_color(WHITE)
        t2[8].align_to(t2[7], LEFT)
        ls = MathTex("\\text{Substract }", "{{\\zeta(s)}}", "-", "\\frac{1}{2^s}","{{\\zeta(s)}}")
        ls.scale(1.25).next_to(lm, DOWN, buff=1, aligned_edge=LEFT)
        ls[3].set_color(RED)
        ts = MathTex(
            r"\left(1-\frac{1}{2^s}\right) \zeta(s)=",
            "1+","\\z{3}+","\\z{5}+","\\z{7}+","\\z{9}+","\\z{11}+","\\cdots",
            tex_template=tz,
            ).scale(1.25).move_to(ls, aligned_edge=LEFT)
        ts[0][3:7].set_color(RED)
        ts[7].align_to(ts[6], LEFT)
        #a
        #1.Zeta Function
        self.play(Write(l1))
        self.play(Write(t1[0]))
        self.play(AnimationGroup(
            *[FadeIn(t1[i], shift=LEFT) for i in range(1,9)],
            lag_ratio=1,
            run_time=4,
            ))
        self.wait(1)
        self.play(ReplacementTransform(t1[8], t1[10]))
        self.wait(1)
        #2.Multiply by
        self.play(Write(lm))
        self.wait(1)
        self.play(FadeOut(lm[0]))
        self.play(lm[1].animate.move_to(tm[0][0:4]))
        self.play(TransformFromCopy(t1[0][0:4], tm[0][4:8]))
        self.play(Write(tm[0][8]))
        self.play(
            AnimationGroup(*[
                AnimationGroup(
                    TransformFromCopy(t1[i], tm[i][0:5]),
                    TransformFromCopy(t1[i][4], tm[i][7]),
                    TransformFromCopy(lm[1], tm[i][5:7]),
                    )
                for i in range(1,5)
                ], lag_ratio=1, run_time=4)
            )
        self.wait(1)
        self.play(tm[1:5].animate.move_to(te[1:5], aligned_edge=RIGHT))
        self.play(
            AnimationGroup(*[
                AnimationGroup(
                    TransformMatchingShapes(tm[i][0:2], te[i][0:2]),
                    ReplacementTransform(tm[i][2:-1], te[i][2:-1]),
                    TransformMatchingShapes(tm[i][-1], te[i][-1]),
                    )
                for i in range(1,5)
                ], lag_ratio=1, run_time=4)
            )
        self.play(
            AnimationGroup(*[
                AnimationGroup(
                    TransformMatchingShapes(te[i][0:2], t2[i][0:2]),
                    ReplacementTransform(te[i][2:-1], t2[i][2:-1]),
                    TransformMatchingShapes(te[i][-1], t2[i][-1]),
                    )
                for i in range(1,5)
                ], lag_ratio=1, run_time=4)
            )
        self.play(AnimationGroup(*[
            FadeIn(t2[i], shift=LEFT)
            for i in range(5,8)
            ], lag_ratio=1))
        self.wait(1)
        self.play(ReplacementTransform(t2[7], t2[8]))
        self.wait(1)
        #3.Substract
        #ls = MathTex("\\text{Substract }", "{{\\zeta(s)}}", "-", "\\frac{1}{2^s}","{{\\zeta(s)}}")
        self.play(Write(ls[0]))
        self.play(AnimationGroup(
            TransformFromCopy(t1[0][0:-1],ls[1]),
            Write(ls[2]),
            TransformFromCopy(t2[0][0:-1],ls[3:]),
            lag_ratio=1,
            ))
        self.wait(1)
        self.play(FadeOut(ls[0]))
        self.play(ls[1:].animate.move_to(ts[0][0:-1], aligned_edge=RIGHT))
        self.wait(1)
        self.play(Write(ts[0][-1]))
        self.wait(1)
        self.play(AnimationGroup(*[
            AnimationGroup(
                TransformFromCopy(t1[i], ts[(i+1)//2]),
                AnimationGroup(Indicate(t1[i+1][0:-1], color=RED), Indicate(t2[(i+1)//2][0:-1], color=RED)),
                lag_ratio=1.25
                )
            for i in range(1,7,2)
            ], lag_ratio=1))
        self.play(TransformFromCopy(t1[7], ts[4]))
        self.play(AnimationGroup(*[
            FadeIn(ts[i], shift=LEFT)
            for i in range(5,7)
            ], lag_ratio=1))
        self.wait(1)
        self.play(Transform(ts[6], ts[7]))
        self.wait(1)
        self.play(ReplacementTransform(ls[1:],ts[0][0:-1]))
        self.wait(2)
        self.play(FadeOut(l1, t1, t2, lm[1], tm[0][4:9]))
        self.wait(1)
        self.play(ts[0:7].animate.to_corner(UL))
        self.wait(2)

        
        #self.next_section("Sum with 3", skip_animations=True)
        p2 = MathTex(
            r"\left(1-\frac{1}{2^s}\right) \zeta(s)=",
            "1+","\\z{3}+","\\z{5}+","\\z{7}+","\\z{9}+",
            "\\z{11}+","\\z{13}+","\\z{15}+","\\z{17}+","\\z{19}+",
            "\\z{21}+","\\z{23}+","\\cdots",
            tex_template=tz,
            ).to_corner(UL)
        p2[0][3:7].set_color(RED)
        p2[13].align_to(p2[8], LEFT)
        l3 = MathTex("\\text{Multiply by }", "\\frac{1}{3^s}").set_color(RED)
        l3.next_to(p2, DOWN, buff=0.75, aligned_edge=LEFT)
        t3 = MathTex(
            r"\frac{1}{3^s}\left(1-\frac{1}{2^s}\right) \zeta(s)=",
            "\\z{3}+","\\z{9}+","\\z{15}+","\\z{21}+","\\z{27}+",
            "\\z{33}+","\\z{39}+","\\cdots",
            tex_template=tz
            ).next_to(p2, DOWN, buff=0.75, aligned_edge=LEFT)
        t3[0][:4].set_color(RED)
        t3[0][7:11].set_color(RED)
        t3[1:].set_color(RED)
        t3[8].align_to(t3[7], LEFT)
        s3 = MathTex(
            "\\text{Substract}",
            "\\left(1-\\frac{1}{2^s}\\right) \\zeta(s)", "-",
            "\\frac{1}{3^s}\\left(1-\\frac{1}{2^s}\\right) \\zeta(s)","=",
            "1",
            tex_template=tz
            ).next_to(t3, DOWN, buff=0.75, aligned_edge=LEFT)
        s3[1][3:7].set_color(RED)
        s3[3][:4].set_color(RED)
        s3[3][7:11].set_color(RED)
        p3 = MathTex(
            "1+", "\\z{5}+", "\\z{7}+", "\\z{11}+", "\\z{13}+", "\\z{17}+",
            "\\z{19}+","\\z{23}+","\\z{25}+","\\z{29}+","\\cdots",
            tex_template=tz
            )
        p3.next_to(s3, DOWN, buff=0.75)
        p3[:-1].to_edge(RIGHT, buff=0)
        #p3.shift(RIGHT*1.5)
        p3[10].align_to(p3[9], LEFT)
        r3 = MathTex(
            r"\left(1-\frac{1}{3^s}\right) \left(1-\frac{1}{2^s}\right) \zeta(s)=",
            "\\frac{1}{2^s}"
            ).next_to(t3, DOWN, buff=0.75, aligned_edge=LEFT)
        r3[0][3:7].set_color(RED)
        r3[0][11:15].set_color(RED)
        #a
        #1. patch with previous scene
        #self.add(ts)
        self.play(
            AnimationGroup(
                ts[:-1].animate.scale(1/1.25).to_corner(UL),
                ReplacementTransform(ts[-2], p2[6:9]),
                rate_func=linear,
                )
            )
        self.wait(1)
        self.play(Transform(p2[8], p2[13]))
        self.wait(1)
        #2. Multiplication
        self.play(Write(l3))
        self.wait(1)
        self.play(FadeOut(l3[0]))
        self.play(l3[1].animate.move_to(t3[0][:4]))
        self.play(TransformFromCopy(ts[0][:-1],t3[0][4:-1]))
        self.play(Write(t3[0][-1]))
        self.play(
            AnimationGroup(
                TransformFromCopy(p2[1][0],t3[1][:2]),
                TransformFromCopy(l3[1][2:],t3[1][2:-1]),
                TransformFromCopy(p2[1][1],t3[1][-1]),
                )
            )
        self.play(
            AnimationGroup(*[
                AnimationGroup(
                    TransformFromCopy(p2[i][:2],t3[i][:2]),
                    TransformFromCopy(l3[1][2:],t3[i][2:-1]),
                    TransformFromCopy(p2[i][-1],t3[i][-1])
                    )
                for i in range(2,8)
                ], lag_ratio=1)
            )
        self.play(Transform(t3[7],t3[8]))
        self.wait(1)
        #3. Substraction
        self.play(Write(s3[0]))
        self.play(
            AnimationGroup(
                TransformFromCopy(ts[0][:-1],s3[1]),
                Write(s3[2]),
                TransformFromCopy(t3[0][:-1],s3[3]),
                Write(s3[4]),
                lag_ratio=1,
                )
            )
        self.play(FadeOut(s3[0]))
        self.play(s3[1:-1].animate.align_to(l3[1], LEFT))#check
        self.wait(1)
        self.play(
            AnimationGroup(
                TransformFromCopy(p2[1],p3[0]),
                AnimationGroup(Indicate(ts[2][:-1], color=RED),Indicate(t3[1][:-1], color=RED)),
                TransformFromCopy(p2[3],p3[1]),
                TransformFromCopy(p2[4],p3[2]),
                AnimationGroup(Indicate(ts[5][:-1], color=RED),Indicate(t3[2][:-1], color=RED)),
                TransformFromCopy(p2[6],p3[3]),
                TransformFromCopy(p2[7],p3[4]),
                lag_ratio=1.25
                )
            )
        self.play(
            AnimationGroup(*[
                FadeIn(p3[i], shift=LEFT)
                for i in range(5,10)
                ], lag_ratio=1)
            )
        self.play(Transform(p3[9],p3[10]))
        self.wait(1)
        self.play(FadeOut(ts[:-2], p2[6:9], l3[1], t3[0][4:], t3[1:8], run_time=2))
        self.wait(1)
        self.play(TransformMatchingShapes(s3[1:-1],r3[0]), run_time=2)
        self.wait(1)
        #self.play(p3.animate.move_to(r3[1], aligned_edge=LEFT))
        self.play(VGroup(r3[0],p3[:10]).animate.to_corner(UL))
        self.wait(2)

        #self.next_section("Sum with 5", skip_animations=True)
        s5 = MathTex(
            r"\left(1-\frac{1}{5^s}\right)",
            r"\left(1-\frac{1}{3^s}\right)",
            r"\left(1-\frac{1}{2^s}\right)", "\\zeta(s)", "=",
            ).next_to(t3, DOWN, aligned_edge=LEFT, buff=0.75)
        for i in range(3):
            s5[i][3:7].set_color(RED)
        p5 = MathTex(
            "1+","\\z{7}+","\\z{11}+","\\z{13}+","\\z{17}+","\\z{19}+",
            "\\z{23}+","\\z{29}+","\\z{31}+","\\z{37}+","\\z{41}+",
            "\\z{43}+","\\z{47}+","\\z{53}+","\\cdots",
            tex_template=tz,
            ).next_to(s5, DOWN, buff=0.75)
        p5[:10].to_edge(RIGHT, buff=0)
        p5[-1].align_to(p5[9], LEFT)
        sa = MathTex(
            r"\left(1-\frac{1}{11^s}\right)",
            r"\left(1-\frac{1}{7^s}\right)",
            r"\left(1-\frac{1}{5^s}\right)",
            r"\left(1-\frac{1}{3^s}\right)",
            r"\left(1-\frac{1}{2^s}\right)", "\\zeta(s)", "=",
            )
        for i in range(2):
            sa[i][5:-2].set_color(BLUE)
        pa = MathTex(
            "1+","\\z{7}+","\\z{11}+","\\z{13}+","\\z{17}+","\\z{19}+",
            "\\z{23}+","\\z{29}+","\\z{31}+","\\cdots","\\z{37}+","\\z{41}+",
            "\\z{43}+","\\z{47}+","\\z{53}+",
            tex_template=tz,
            )
        for i in range(10,15):
            pa[i][2:-2].set_color(BLUE)
        la = Tex("Prime numbers", color=BLUE)
        ga = VGroup(sa,pa,la).arrange(direction=DOWN, buff=0.75)
        sa.align_to(s5, RIGHT)
        pa.align_to(p5, LEFT)
        for i in range(2):
            sa[i].align_to(s5[0],RIGHT)
        ca = MathTex(
            "1+","\\z{13}+","\\z{17}+","\\z{19}+","\\z{23}+","\\z{29}+","\\z{31}+",
            "\\z{37}+","\\z{41}+","\\cdots",
            tex_template=tz,
            )
        ca.move_to(pa, aligned_edge=LEFT)
        #a
        self.play(Write(s5[0]))
        self.play(TransformFromCopy(r3[0][:-1], s5[1:-1]))
        self.play(Write(s5[-1]))
        #"1+", "\\z{5}+", "\\z{7}+", "\\z{11}+", "\\z{13}+", "\\z{17}+","\\z{19}+","\\z{23}+","\\z{25}+","\\z{29}+","\\cdots",
        self.play(
            AnimationGroup(
                TransformFromCopy(p3[0],p5[0]),
                Indicate(p3[1][:-1], color=RED),
                #TransformFromCopy(p3[2:8],p5[1:7]),
                AnimationGroup(*[
                    TransformFromCopy(p3[i+1],p5[i])
                    for i in range(1,7)
                    ],lag_ratio=1),
                Indicate(p3[8][:-1], color=RED),
                lag_ratio=1,
                )
            )
        self.play(
            AnimationGroup(*[
                FadeIn(p5[i], shift=LEFT) for i in range(7,10)
                ], lag_ratio=1)
            )
        self.play(Transform(p5[9],p5[-1]))
        self.wait(2)
        self.play(FadeOut(r3[0], p3[:10]))
        self.wait(1)
        self.play(
            s5.animate.move_to(sa[2:]),
            p5[:10].animate.move_to(pa[:10]),
            )
        self.play(
            FadeOut(s5, p5[:10]),
            FadeIn(sa[2:], pa[:10]),
            )
        self.wait(1)
        self.play(
            AnimationGroup(*[
                Succession(
                    sa[5-i][5].animate.set_color(BLUE),
                    Indicate(sa[5-i][5], color=BLUE),
                    )
                for i in range(1,4)
                ], lag_ratio=1, run_time=2, rate_func=linear)
            )
        self.play(
            AnimationGroup(*[
                Succession(
                    pa[i][2:-2].animate.set_color(BLUE),
                    Indicate(pa[i][2:-2], color=BLUE),
                    )
                for i in range(1,9)
                ], lag_ratio=1, run_time=4, rate_func=linear)
            )
        self.play(Wiggle(la))
        self.wait(1)
        self.play(sa[2:].animate.align_to(s5[1:], LEFT))
        self.play(TransformMatchingShapes(pa[1],sa[1]))
        self.play(
            AnimationGroup(
                pa[2:9].animate.align_to(pa[1], LEFT),
                pa[10].animate.align_to(ca[8], LEFT),
                pa[9].animate.align_to(ca[9], LEFT)
                )
            )
        self.play(sa[1:].animate.align_to(s5[1:], LEFT))
        self.play(TransformMatchingShapes(pa[2],sa[0]))
        self.play(
            AnimationGroup(
                pa[3:9].animate.align_to(pa[1], LEFT),
                pa[10].animate.align_to(ca[7], LEFT),
                pa[11].animate.align_to(ca[8], LEFT),
                )
            )
        self.wait(1)
        self.play(FadeOut(la))
        self.wait(2)

        #self.next_section("to infinity")
        #m
        sh = MathTex(
            r"\left(1-\frac{1}{997^s}\right)",
            r"\left(1-\frac{1}{991^s}\right)",
            "\\cdots",
            r"\left(1-\frac{1}{3^s}\right)",
            r"\left(1-\frac{1}{2^s}\right)", "\\zeta(s)", "=",
            )
        for i in range(2):
            sh[i][5:-2].set_color(BLUE)
        for i in range(3,5):
            sh[i][5:-2].set_color(BLUE)
        ph = MathTex(
            "1+","\\z{1009}+","\\z{1013}+","\\z{1019}+","\\z{1021}+","\\z{1031}+","\\z{1033}+",
            "\\cdots",
            tex_template=tz,
            )
        for i in range(1,7):
            ph[i][2:-2].set_color(BLUE)
        lh = MathTex(
            "\\text{If }s >1"
            )
        gh = VGroup(sh,ph,lh).arrange(direction=DOWN, buff=0.75)
        sh.to_edge(LEFT)
        ph.to_edge(RIGHT)
        e3 = MathTex(
            "1+","\\frac{1}{1009^3}+","\\frac{1}{1013^3}+","\\frac{1}{1019^3}+","\\frac{1}{1021^3}+",
            "\\frac{1}{1031^3}+","\\frac{1}{1033^3}+",
            "\\cdots",
            tex_template=tz,
            ).move_to(ph)
        for i in range(1,7):
            e3[i][-2].set_color(YELLOW)
        ih = MathTex("\\text{For example }", "s=", "3").set_color(YELLOW).move_to(lh)
        n3 = DecimalNumber(
            1.000000067310360815341,
            num_decimal_places=20,
            show_ellipsis=True,
            ).move_to(ph)
        li = Tex("With infinite prime numbers").set_color(BLUE).move_to(lh)
        si = MathTex(
            "\\cdots",
            r"\left(1-\frac{1}{7^s}\right)",
            r"\left(1-\frac{1}{5^s}\right)",
            r"\left(1-\frac{1}{3^s}\right)",
            r"\left(1-\frac{1}{2^s}\right)", "\\zeta(s)", "=", "1",
            "\\cfrac{1}{1-\\cfrac{1}{2^s}}",
            ).move_to(sh, aligned_edge=UP).to_edge(LEFT)
        si[8:].align_to(si[7], LEFT)
        for i in range(1,5):
            si[i][5:-2].set_color(BLUE)
        si[8][6].set_color(BLUE)
        sj = MathTex(
            "\\zeta(s)", "=",
            "\\cfrac{1}{1-\\cfrac{1}{2^s}}",
            "\\times\\cfrac{1}{1-\\cfrac{1}{3^s}}",
            "\\times\\cfrac{1}{1-\\cfrac{1}{5^s}}",
            "\\times\\cfrac{1}{1-\\cfrac{1}{7^s}}",
            "\\times\\cdots"
            )
        sg = VGroup()
        for i in range(4):
            sg.add(sj.copy())
            sg[i].move_to(si[5:])
            sg[i].align_to(si[4-i], LEFT)
            sg[i][2][6].set_color(BLUE)
            for j in range(3,6):
                sg[i][j][7:-1].set_color(BLUE)
        sn = MathTex(
            "\\zeta(s)", "=",
            "\\cfrac{1}{1-2^{-s}}",
            "\\times\\cfrac{1}{1-3^{-s}}",
            "\\times\\cfrac{1}{1-5^{-s}}",
            "\\times\\cfrac{1}{1-7^{-s}}",
            "\\times\\cdots"
            ).move_to(sg[3], aligned_edge=LEFT).align_to(sg[3], UP)
        sn[2][4].set_color(BLUE)
        for i in range(3,6):
            sn[i][5:-2].set_color(BLUE)
        sr = MathTex(
            "\\zeta(s)", "=",
            "\\left(1-2^{-s}\\right)^{-1}",
            "\\left(1-3^{-s}\\right)^{-1}",
            "\\left(1-5^{-s}\\right)^{-1}",
            "\\left(1-7^{-s}\\right)^{-1}",
            "\\cdots"
            ).move_to(sg[3], aligned_edge=LEFT).align_to(sg[3][0], UP)
        sr.to_edge(LEFT)
        for i in range(2,6):
            sr[i][3:-5].set_color(BLUE)
        pr = MathTex(
            "\\zeta(s)", "=",
            "\\prod_{p}","\\left(1-p^{-s}\\right)^{-1}"
            ).next_to(si, DOWN)
        pr[2][1].set_color(BLUE)
        pr[3][3].set_color(BLUE)
        su = MathTex(
            "\\sum_{n}", "n^{-s}", "=1"
            ).scale(1.75).to_edge(LEFT)
        #a
        self.play(
            AnimationGroup(
                FadeOut(sa[:3], shift=RIGHT),
                TransformMatchingShapes(sa[3:], sh[3:]),
                FadeIn(sh[:3], shift=RIGHT),
                TransformMatchingShapes(pa[9], ph[7]),
                TransformMatchingShapes(pa[0], ph[0]),
                FadeOut(pa[3:9], pa[10:12], shift=LEFT),
                FadeIn(ph[1:], shift=LEFT),
                rate_func=linear,
                run_time=3,
                )
            )
        self.play(Write(lh))
        self.play(ReplacementTransform(lh, ih))
        self.wait(1)
        self.play(
            AnimationGroup(
                TransformMatchingShapes(ph[0],e3[0]),
                AnimationGroup(*[TransformMatchingShapes(ph[i][:-2], e3[i][:-2]) for i in range(1,7)]),
                AnimationGroup(*[FadeOut(ph[i][-2]) for i in range(1,7)]),
                AnimationGroup(*[TransformMatchingShapes(ph[i][-1], e3[i][-1]) for i in range(1,7)]),
                TransformMatchingShapes(ph[-1],e3[-1]),
                )
            )
        self.play(
            AnimationGroup(*[TransformFromCopy(ih[2], e3[i][-2]) for i in range(1,7)])
            )
        self.wait(1)
        self.play(ReplacementTransform(e3, n3))
        self.wait(1)
        self.play(ReplacementTransform(ih, li))
                
        self.play(
            AnimationGroup(
                FadeOut(sh[:3], shift=RIGHT),
                AnimationGroup(*[TransformMatchingShapes(sh[3:], si[3:-2])]),
                FadeIn(si[:3],shift=RIGHT),
                )
            )
        self.play(n3.animate.set_value(1))
        self.play(ReplacementTransform(n3,si[7]))
        self.play(FadeOut(li))
        self.play(
            AnimationGroup(
                TransformMatchingShapes(si[7], si[8][0]),
                Write(si[8][1]),
                TransformMatchingShapes(si[4], si[8][2:]),
                lag_ratio=1
                )
            )
        self.play(
            TransformMatchingShapes(si[5:7], sg[0][:2]),
            TransformMatchingShapes(si[8], sg[0][2]),
            )

        for i in range(3,6):
            self.play(
                AnimationGroup(
                    Write(sg[i-3][i][0]),
                    FadeIn(sg[i-3][i][1], shift=RIGHT),#TransformFromCopy(sg[0][2][0], sg[i-3][i][1]),
                    Write(sg[i-3][i][2]),
                    FadeOut(si[6-i][0], si[6-i][-1]),
                    #TransformMatchingShapes(si[6-i], sg[i-3][i][3:]),
                    AnimationGroup(
                        TransformMatchingShapes(si[6-i][1], sg[i-3][i][3]),
                        ReplacementTransform(si[6-i][2], sg[i-3][i][4]),
                        TransformMatchingShapes(si[6-i][3:-1], sg[i-3][i][5:]),
                        ),
                    lag_ratio=0.5
                    )
                )
            self.play(TransformMatchingShapes(sg[i-3][:i+1], sg[i-2][:i+1]))
        self.play(Write(sg[3][6][0]))
        #self.play(ReplacementTransform(si[0], sg[3][6][1]))
        self.play(
            AnimationGroup(FadeOut(si[0], shift=RIGHT), FadeIn(sg[3][6][1:], shift=RIGHT))
            )
        self.wait(1)
        self.play(sg[3][2:].animate.move_to(sg[2][2:]))
        self.play(
            AnimationGroup(*[
                TransformMatchingShapes(sg[3][i], sn[i])
                for i in range(7)
                ], lag_ratio=1)
            )
        self.wait(1)
        self.play(sn[2:].animate.to_edge(RIGHT))
        self.play(
            AnimationGroup(*[
                TransformMatchingShapes(sn[i], sr[i])
                for i in range(7)
                ], lag_ratio=1)
            )
        self.wait(1)
        self.play(
            AnimationGroup(
                TransformMatchingShapes(sr[0], pr[0]),
                TransformMatchingShapes(sr[1], pr[1]),
                Write(pr[2]),
                AnimationGroup(*[TransformMatchingShapes(sr[i][:3], pr[3][:3]) for i in range(2,6)]),
                AnimationGroup(*[ReplacementTransform(sr[i][3:6], pr[3][3:6]) for i in range(2,6)]),
                AnimationGroup(*[TransformMatchingShapes(sr[i][6:], pr[3][6:]) for i in range(2,6)]),
                FadeOut(sr[-1]),
                lag_ratio=1,
                )
            )
        self.play(pr.animate.move_to(ORIGIN).scale(1.75))
        self.wait(2)
        self.play(TransformMatchingShapes(pr[0], t1[0]))
        self.play(FadeIn(t1[1:8], t1[-1]))
        self.wait(1)
        self.play(Write(su[0]))
        self.play(pr[1:].animate.align_to(su[2:], LEFT))
        self.play(AnimationGroup(*[ReplacementTransform(t1[i], su[1]) for i in range(1,8)]))
        self.play(FadeOut(t1[:8], t1[-1]))
        self.play(VGroup(su[0:2], pr[1:]).animate.move_to(ORIGIN))
        self.wait(2)