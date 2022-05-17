within DymolaExamples.Examples_Filters;
model Chebyshev
  Modelica.Blocks.Continuous.Filter Filter(
    normalized=false,
    analogFilter=Modelica.Blocks.Types.AnalogFilter.ChebyshevI,
    init=Modelica.Blocks.Types.Init.InitialState,
    filterType=Modelica.Blocks.Types.FilterType.LowPass,
    order=2,
    f_cut=1,
    f_min=0.8*1,
    x_start={0,y_start})
    annotation (Placement(transformation(extent={{-34,2},{-14,22}})));
  Modelica.Blocks.Interfaces.RealInput u1
              "Connector of Real input signal"
    annotation (Placement(transformation(extent={{-140,-8},{-100,32}})));
  Modelica.Blocks.Interfaces.RealOutput y1
               "Connector of Real output signal"
    annotation (Placement(transformation(extent={{100,2},{120,22}})));
  parameter Real y_start=0
    "Initial or guess values of states";
equation
  connect(Filter.u, u1)
    annotation (Line(points={{-36,12},{-120,12}}, color={0,0,127}));
  connect(Filter.y, y1)
    annotation (Line(points={{-13,12},{110,12}}, color={0,0,127}));
  annotation (Icon(coordinateSystem(preserveAspectRatio=false)), Diagram(
        coordinateSystem(preserveAspectRatio=false)));
end Chebyshev;
