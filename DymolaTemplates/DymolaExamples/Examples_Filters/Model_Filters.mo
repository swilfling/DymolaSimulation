within DymolaExamples.Examples_Filters;
model Model_Filters
  Modelica.Blocks.Continuous.Filter CriticalDamping(
    analogFilter=Modelica.Blocks.Types.AnalogFilter.CriticalDamping,
    normalized=normalized,
    filterType=filterType,
    order=order,
    f_cut=f_cut,
    f_min=0.8*f_cut)
    annotation (Placement(transformation(extent={{-48,46},{-28,66}})));
  Modelica.Blocks.Continuous.Filter Bessel(
    normalized=normalized,
    analogFilter=Modelica.Blocks.Types.AnalogFilter.Bessel,
    init=init,
    filterType=filterType,
    order=order,
    f_cut=f_cut,
    f_min=0.8*f_cut)
    annotation (Placement(transformation(extent={{-48,12},{-28,32}})));
  Modelica.Blocks.Continuous.Filter Butterworth(
    normalized=normalized,
    analogFilter=Modelica.Blocks.Types.AnalogFilter.Butterworth,
    init=init,
    filterType=filterType,
    order=order,
    f_cut=f_cut,
    f_min=0.8*f_cut)
    annotation (Placement(transformation(extent={{-48,-26},{-28,-6}})));
  Modelica.Blocks.Continuous.Filter ChebyshevI(
    normalized=normalized,
    analogFilter=Modelica.Blocks.Types.AnalogFilter.ChebyshevI,
    init=init,
    filterType=filterType,
    order=order,
    f_cut=f_cut,
    f_min=0.8*f_cut)
    annotation (Placement(transformation(extent={{-48,-62},{-28,-42}})));
  parameter Real f_cut=2 annotation (Dialog(group="Filter Parameters"));
  parameter Boolean normalized=false
    annotation (Dialog(group="Filter Parameters"));
  parameter Integer order=2 annotation (Dialog(group="Filter Parameters"));
  parameter Modelica.Blocks.Types.FilterType filterType=Modelica.Blocks.Types.FilterType.LowPass
    annotation (Dialog(group="Filter Parameters"));
  Modelica.Blocks.Interfaces.RealInput u
    annotation (Placement(transformation(extent={{-98,48},{-80,66}}),
        iconTransformation(extent={{-98,48},{-80,66}})));
  parameter Modelica.Blocks.Types.Init init=Modelica.Blocks.Types.Init.SteadyState
    annotation (Dialog(group="Filter Parameters"));
  Modelica.Blocks.Interfaces.RealOutput y
    annotation (Placement(transformation(extent={{82,8},{102,28}})));
  Modelica.Blocks.Routing.Extractor extractor(
    nin=4,
    allowOutOfRange=true,
    outOfRangeValue=1)
    annotation (Placement(transformation(extent={{48,8},{68,28}})));
  Modelica.Blocks.Routing.Multiplex4 multiplex4_1
    annotation (Placement(transformation(extent={{6,8},{26,28}})));
  Modelica.Blocks.Interfaces.IntegerInput select
    annotation (Placement(transformation(extent={{-100,-86},{-82,-68}}),
        iconTransformation(extent={{-100,-86},{-82,-68}})));
equation
  connect(Bessel.u, u) annotation (Line(points={{-50,22},{-70,22},{-70,57},{
          -89,57}},  color={0,0,127}));
  connect(Butterworth.u, u) annotation (Line(points={{-50,-16},{-70,-16},{-70,
          57},{-89,57}},  color={0,0,127}));
  connect(ChebyshevI.u, u) annotation (Line(points={{-50,-52},{-70,-52},{-70,
          57},{-89,57}},  color={0,0,127}));
  connect(CriticalDamping.u, u) annotation (Line(points={{-50,56},{-70,56},{
          -70,57},{-89,57}},
                         color={0,0,127}));

  connect(multiplex4_1.u1[1], CriticalDamping.y) annotation (Line(points={{4,27},{
          -11,27},{-11,56},{-27,56}},      color={0,0,127}));
  connect(multiplex4_1.u2[1], Bessel.y) annotation (Line(points={{4,21},{-12,
          21},{-12,22},{-27,22}}, color={0,0,127}));
  connect(multiplex4_1.u3[1], Butterworth.y) annotation (Line(points={{4,15},
          {-12,15},{-12,-16},{-27,-16}}, color={0,0,127}));
  connect(multiplex4_1.u4[1], ChebyshevI.y) annotation (Line(points={{4,9},{
          -6,9},{-6,-52},{-27,-52}},   color={0,0,127}));

  connect(extractor.u, multiplex4_1.y)
    annotation (Line(points={{46,18},{27,18}}, color={0,0,127}));
  connect(extractor.index, select) annotation (Line(points={{58,6},{58,-77},{-91,
          -77}},      color={255,127,0}));
  connect(extractor.y, y)
    annotation (Line(points={{69,18},{92,18}}, color={0,0,127}));

  annotation (experiment(StopTime=1, __Dymola_Algorithm="Dassl"));
end Model_Filters;
